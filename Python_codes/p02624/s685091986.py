#Osa_k法（前処理をした後、素因数分解をO(logN)でできる）

N = int(input())
sieve = [-1] * (N+1)
#prime = []
for i in range(2, N+1):#前処理（各indexについて、割れる最小の素数）
    if sieve[i] == -1:#未探索のとき
        sieve[i] = i
        #prime.append(i)#素数列挙したいとき
        for j in range(i*i, N+1, i):
            if sieve[j] == -1:
                sieve[j] = i
#print(sieve)
#print(prime)

Ans = [1] * (N+1)
for i in range(2, N+1):
    p = sieve[i]
    cur = i
    cnt = 0
    while cur > 1:
        if cur % p == 0:
            cur //= p
            cnt += 1
        else:
            break
    if i == pow(p,cnt):#iの素因数がpのみ
        Ans[i] = i*(cnt+1)
    else:
        Ans[i] = Ans[i//(p**cnt)] * Ans[p**cnt]#それ以外の時、掛算すればOK
#print(Ans)
print(sum(Ans)-1)