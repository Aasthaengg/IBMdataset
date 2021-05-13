N,A,B = map(int,input().split())

ans = 0
for i in range(1,N+1):
    a = int(i/10000)%10
    b = int(i/1000)%10
    c = int(i/100)%10
    d = int(i/10)%10
    e = i%10
    
    if A<=a+b+c+d+e and a+b+c+d+e<=B:
        ans += i
        
print(ans)