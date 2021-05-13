n,limit = map(int,input().split())
a = list(map(int, input().split()))

su = 0
for i in range(n):
    su += a[i]

factors = set()

for i in range(1,int(su**0.5)+1):
    if su%i == 0:
        factors.add(i)
        factors.add(int(su/i))

factors = list(factors)
factors = sorted(factors)

def check(k):
    #print(str(k)+"をチェックします")
    n_sum = 0
    p_sum = 0
    nas = []
    pas = []
    for i in range(n):
        na = a[i]%k
        pa = k-na
        n_sum += na
        p_sum += pa
        nas.append(na)
        pas.append(pa)
    if n_sum%k != 0:
        return 0
    nas = sorted(nas)
    pas = sorted(pas)
    #print(nas)
    #print(pas)
    
    s_nas = []
    s_pas = []
    su_nas = 0
    su_pas = 0
    for i in range(n):
        su_nas += nas[i]
        su_pas += pas[i]
        s_nas.append(su_nas)
        s_pas.append(su_pas)
    #print(s_nas)
    #print(s_pas)
        
    for i in range(n):
        if s_nas[i] == s_pas[n-i-2] and s_nas[i] <= limit:
            #print(s_nas[i],s_pas[n-i-2])
            return 1
    return 0


ma = 1
#print(factors)

for i in range(len(factors)):
    if (check(factors[i])):
        ma = factors[i]

print(ma)