N,A,B = map(int,input().split())
ans = 0
for i in range(1,N+1) :
    ix = sum(list(map(int,list(str(i)))))
    if A<= ix and ix <= B :
        ans += i
print(ans)