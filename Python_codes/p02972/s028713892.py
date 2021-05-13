import sys

input = sys.stdin.readline

def main():
    N = int(input())
    a = [0] + list(map(int, input().split()))

    box = [0] * (N+1)
    for i in range(N, 0, -1):
        tmp = sum(box[i::i])
        if tmp%2 == a[i]:
            continue
        else:
            box[i] = 1
    ans = []
    for i in range(1, N+1):
        if box[i] == 1:
            ans.append(i)
    print(sum(box))
    if len(ans) != 0:
        print(*ans)

if __name__ == "__main__":
    main()
