N=int(input())

# X以下のnの約数の個数
def g(n,X):
    m=X//n
    s=(m*(m+1)//2)*n
    return s

ans=0
for i in range(1,N+1):
    ans += g(i,N)
    # print(g(i,N))
print(ans)