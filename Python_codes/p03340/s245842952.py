import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    """
    条件成立＝（２進数表示した時に各桁に１が高々1つしか登場しない）
    なので尺取り法でいけそう
    """
    left = 0
    right = 1
    bit = {i for i in range(20) if A[0] & (1 << i)}

    ans = 0
    while right <= N:
        #print("[{}, {}) -> {}".format(left, right, right - left))
        ans += right - left
        if right == N:
            print(ans)
            return

        bit_right = {i for i in range(20) if A[right] & (1 << i)}
        while bit & bit_right:
            bit_left = {i for i in range(20) if A[left] & (1 << i)}
            bit -= bit_left
            left += 1
        bit |= bit_right
        right += 1



if __name__ == "__main__":
    main()
