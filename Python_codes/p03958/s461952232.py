import heapq
k,t = map(int,input().split())
a = list(map(int,input().split()))
mx = max(a)
others = k - mx
if t == 1:
    print(k - 1)
    exit()

if others >= mx - 1:
    print(0)
else:
    print(mx - others - 1)
