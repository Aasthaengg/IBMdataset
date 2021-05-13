n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))

t = [0]+t+[t[-1]]
a = [a[0]]+a+[0]

ans = 1

for i in range(1,n+1):
    if t[i]==t[i-1] and a[i]==a[i+1]:
        ans *= min(t[i],a[i])
        ans %= 10**9+7
    elif t[i]!=t[i-1] and a[i]!=a[i+1]:
        if t[i]!=a[i]:
            print(0)
            exit()
    elif t[i]!=t[i-1] and t[i]>a[i]:
        print(0)
        exit()
    elif a[i]!=a[i+1] and a[i]>t[i]:
        print(0)
        exit()

print(ans)