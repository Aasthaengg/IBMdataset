k = int(input())

if k%2 == 0 or k%5 == 0:
    print(-1)

else:
    ans = -1
    a = 7
    
    if k == 7 or k==1:
        print(1)
    
    else:
        for i in range(2,10**7):
            a = (10*a + 7)%k
            if a==0:
                ans =i
                break
        
        print(ans)