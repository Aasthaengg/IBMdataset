n = int(input())
t = list(map(int,input().split()))
a = list(map(int,input().split()))
ans = 1
mod = 10**9+7
if (not a[0] == t[n-1]):
    print(0)
    exit()

for i in range(1,n-1):
    if ((not t[i] == t[i-1]) and t[i] > a[i]) or ((not a[i] == a[i+1]) and a[i] > t[i]):
        print(0)
        exit()
    elif t[i] == t[i-1] and a[i] == a[i+1]:
        ans = (ans*min(t[i],a[i]))%mod

print(ans)
