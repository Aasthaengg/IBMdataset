n = int(input())
a = input()
b = input()
ans = 1
i = 0
wari = 1000000007
if n == 1:
    print(3)
    exit()
elif n == 2:
    print(6)
    exit()
else:
    if a[i] == b[i]:
        ans *=3
        i +=1
        
    else:
        i +=2
        ans *=6
        
    while True:
        if i >= n:
            break
        if a[i-1] == b[i-1]:
            if a[i] == b[i]:
                ans*=2
                ans%=wari
                i+=1
            else:
                ans*=2
                ans%=wari
                i+=2
        else:
            if a[i] == b[i]:
                ans*=1
                ans%=wari
                i+=1
            else:
                ans*=3
                ans%=wari
                i+=2
    print(ans)