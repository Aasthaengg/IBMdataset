import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7

a.sort(reverse = True)

#l = len(bin(a[0])[2:])

ans  = 0
for b in range(60+1):
    count_1 = 0
    count_0 = 0
    for i in range(n):
        if (a[i] >> b) & 1:
            count_1 += 1
        else:
            count_0 += 1
    count_1 %= mod
    count_0 %= mod
    ans += (count_1 * count_0 * pow(2,b,mod))%mod


print(ans%mod)