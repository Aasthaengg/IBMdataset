import sys


def input():
    return sys.stdin.readline().strip()


N = int(input())
B = list(map(int, input().split()))
hand = []


def check(B, cnt):
    n = len(B)
    for i in range(n):
        if B[n - i - 1] == (n - i):
            hand.append(B[n - i - 1])
            B = B[: n - i - 1] + B[n - i :]
            break
    if len(B) != n and len(B) > 0:
        return B
    else:
        return False


cnt = 1
while B:
    B = check(B, cnt)
    # print(B)

if len(hand) < N:
    print(-1)
    sys.exit()
answer = hand[::-1]
for i in range(N):
    if answer[i] > i + 1:
        print(-1)
        sys.exit()
print(*answer, sep="\n")
