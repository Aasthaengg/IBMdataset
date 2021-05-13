n,a,b = map(int,input().split())
cnt = 0

for i in range(n+1):
    ans = 0
    tmp = i
    while(tmp>0):
        ans += tmp%10
        tmp = tmp//10
        #print(ans, tmp)
    
    if(a<=ans and ans<=b):
        cnt+=i

print(cnt)

