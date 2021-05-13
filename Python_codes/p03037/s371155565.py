n,m = map(int,input().split())
a = []
b = []
for i in range(m):
    A,B = map(int,input().split())
    a.append(A)
    b.append(B)
    
ans = min(b) - max(a) + 1
print(max(ans,0))