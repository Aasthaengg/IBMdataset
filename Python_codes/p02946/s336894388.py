K , X =(int(a) for a in input().split())
n = 2*K -1
ans = []
for i in range(1,n+1) :
    ans.append(X-K+i)

print(*ans)