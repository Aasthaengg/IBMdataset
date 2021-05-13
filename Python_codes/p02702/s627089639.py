import sys
def input():
    return sys.stdin.readline()[:-1]


def main():
    S = input()[::-1] # 入力文字列を逆順で格納
    counts = [0] * 2019
    counts[0] = 1
    num, d = 0, 1

    for char in S:
        num = num + int(char) * d
        num = num % 2019
        d = d * 10
        d = d % 2019
        counts[num] += 1 #余りの数の番号のリストに+1していくことでカウント

    ans = 0
    for cnt in counts:
        ans += cnt * (cnt - 1) // 2
    print(ans)

    
if __name__ == "__main__":
    main()