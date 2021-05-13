n = int(input())
DIV=10**9+7
s=1
for i in range(1,n+1):
    s=(s*i)%int(DIV)
print(s)