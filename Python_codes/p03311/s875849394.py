N = int(input())

A = list(map(int,input().split()))

memo = []

for key,val in enumerate(A):
    memo.append(val-key-1)

memo.sort()

b = memo[len(memo)//2]

ans  = 0
for key,val in enumerate(A):
    ans += abs(val-(b+key+1))

print(ans)