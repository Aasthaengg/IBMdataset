def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


A = input()
L = len(A)


def ctoi(char):
    return ord(char) - 97


cnt = [0] * 26

for a in A:
    cnt[ctoi(a)] += 1

ans = 1 + (L * (L - 1)) // 2
for n in cnt:
    ans -= (n * (n - 1)) // 2

print(ans)