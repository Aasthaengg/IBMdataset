import collections as col

def prime(n):
    ans = []
    for i in range(2, int(n**0.5)+1):
        while not n%i: n //= i ; ans.append(i)
    if n != 1: ans.append(n)
    return col.Counter(ans)
    
n = int(input())
a = list(map(int,input().split()))

cnt = col.Counter()
for num in a:
    new = prime(num)
    for key,val in new.items():
        if val > cnt[key] : cnt[key] = val

LCM = 1
MOD = 10**9 + 7
for key,val in cnt.items(): LCM *= key**val %MOD

ans = 0
for num in a:
    b = LCM * pow(num, MOD-2, MOD) #割るのではなく逆元をかける
    ans += b
    
print(ans%MOD)



