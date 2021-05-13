import collections
N = int(input())
A = list(map(int,input().split()))

count = collections.Counter(A)
ans = []

for i in range(1,N+1):
    ans.append(count[i])
    
    
[print(x) for x in ans]