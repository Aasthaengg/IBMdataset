from operator import itemgetter
n,k = map(int,input().split())
count = 0
ans = 0
a = [list(map(int,input().split())) for i in range(n)]
number = sorted(a, key = lambda x: x[0])

for i in range(n):
    count += number[i][1]
    if count >= k:
        ans = number[i][0]
        break
    
print(ans)