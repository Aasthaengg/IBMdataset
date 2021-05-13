n=int(input())

t = list(map(int,input().split()))

t.sort()

memo = []
check = 1
for i in range(n-1):
    if t[i] == t[i+1] and i == n-2:
        check += 1
        memo.extend([t[i]]*(check//2))
    elif t[i] == t[i+1]:
        check += 1
    elif t[i] != t[i+1] and check>1:
        memo.extend([t[i]]*(check//2))
        check = 1

memo.sort(reverse=True)

if len(memo)>1:
    print(memo[0]*memo[1])
else:
    print(0)