n = int(input())
t = list(map(int,input().split()))
a = list(map(int,input().split()))
if n == 1:
    if t[0] == a[0]:
        print(1)
    else:
        print(0)
elif n == 2:
    if t[0] >= a[1]:
        if t[0] == t[1] and a[0] >= a[1]:
            if t[0] == a[0]:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        if t[0] < t[1] and a[0] == a[1] and a[1] == t[1]:
            print(1)
        else:
            print(0)
else:
    mod = 10**9 + 7
    ans = 1
    for i in range(1,n-1):
        if t[i-1] == t[i]:
            if a[i+1] == a[i]:
                ans = (ans*(min((a[i],t[i]))%mod)) % mod
            else:
                if a[i] > t[i]:
                    ans = 0
                    break
        else:
            if a[i] < t[i]:
                ans = 0
                break
    if t[0] > a[0] or t[n-1] < a[n-1]:
        ans = 0
    print(ans)