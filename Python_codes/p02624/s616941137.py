import sys
input = sys.stdin.readline

n = int(input())
cnt = [2]*(n+1)

cnt[1] = 1

for i in range(2,n+1):
    for j in range(i*2,n+1,i):
        cnt[j] += 1

res = 0

for i in range(n+1):
    res += cnt[i]*i
print(res)