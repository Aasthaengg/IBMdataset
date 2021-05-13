def cnt_facts(n):
    a = 2
    lst = []
    while a**2 <= n:
        if n % a == 0:
            ex = 0
            while n % a == 0:
                ex += 1
                n //= a
            lst.append([a, ex])
        a += 1
    
    if n != 1: lst.append([n,1])
    
    return lst

n = int(input())
ans_d = {} #素因数分解を格納する辞書
for i in range(2,n+1): #n! の1,2,3...,n-1, nを順に素因数分解し、結果を統合
    l = cnt_facts(i)
    for i in l:
        k = i[0] #素数
        v = i[1] #指数
        if k not in ans_d:
            ans_d[k] = v
        else:
            ans_d[k] += v

#print(ans_d)
mod = 10**9 + 7
ans = 1
for v in ans_d.values():
    ans *= v + 1
print(ans%mod)