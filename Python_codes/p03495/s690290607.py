from collections import Counter, deque, defaultdict
n, k = map(int, input().split())
A = list(map(int, input().split()))
t = defaultdict(int)
for x in A:
    t[x]+=1
B = []
for x in t.values():
    B.append(x)
B.sort()
if(len(B)<=k):
    print(0)
    exit()
    
ans = 0
for i in range(0, len(B)):
    ans+=B[i]
    if len(B)-(i+1) <= k:
        break
print(ans)
