A,B = map(int, input().split())

ans = 0
for i in range(A,B+1):
    if int(i/10000)==i%10 and int(i/1000)%10 == int(i/10)%10:
        ans+=1
        
print(ans)