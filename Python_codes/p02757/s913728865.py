from collections import defaultdict

n, p = map(int,input().split())
s = input()

res = 0

if p not in [2,5]:
    crem = 0
    
    crem_10 = [1]
    for i in range(1,n):
        crem_10 += [(crem_10[-1] * (10%p)) % p]
        
    dic_p = defaultdict(lambda : 0)
    for i,subs in enumerate(s[::-1]):
        crem += (int(subs) % p * crem_10[i]) % p
        crem %= p

        if crem == 0:
            res += 1
        res += dic_p[crem]

        dic_p[crem] += 1
        
else:
    for i,subs in enumerate(s[::-1]):
        if int(subs) % p == 0:
            res += n - i
    
print(res)