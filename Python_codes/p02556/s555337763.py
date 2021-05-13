N = int(input())
A = []
B = []
for i in range(N):
    x,y = map(int,input().split())
    A.append(x+y)
    B.append(x-y)

a = max(A)
b = min(A)
c = max(B)
d = min(B)

ans = max(a-b,c-d)
print(ans)