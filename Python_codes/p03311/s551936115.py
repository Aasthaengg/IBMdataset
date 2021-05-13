N = int(input())
A = list(map(int,input().split()))

memo = []

for key,val in enumerate(A):
    memo.append(val-key-1)
memo.sort()

ans = 0
for key,val in enumerate(A):
    ans += abs(val-key-1-memo[N//2])
print(ans)