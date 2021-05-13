n,m = map(int,input().split())
l = [[int(x) for x in input().split()[1:]] for i in range(m)]
odd_even = [int(x) for x in input().split()]


num = 0
limit = 2**n
ans = 0
while(num < limit):
    
    isOK = True
    for i in range(m):
        cnt = 0
        for x in l[i]:
            if((num >> (x-1)) & 1):
                cnt += 1
        
        if(cnt%2!=odd_even[i]):
            isOK = False
            break        
        
    if(isOK):
        ans += 1    
    
    num += 1

print(ans)