n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0

def dm(i, j):
    d = min(a[i], b[j])
    a[i] -= d; b[j] -= d
    return d

for i in range(n):
    cnt += dm(i, i)
    cnt += dm(i + 1, i)
print(cnt)