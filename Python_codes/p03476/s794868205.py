def prime_checker_range(n): #n未満の数の中で素数のものを全て出力(リスト型)
    ls = [i for i in range(2,n)]
    p = 0
    while True:
        new_ls = [j for j in ls if (j % ls[p] != 0) or (j <= ls[p])]
        ls = new_ls
        if ls[p]**2 >= max(ls):
            return ls
        else:
            p += 1
    return ls
def prime_checker(i): #素数かどうか判定
    if i == 1:
        return False
    else:
        for j in range(2,(int(i**0.5))+1):
            if i % j == 0:
                return False
            else:
                continue
        return True
q = int(input())
ls = [i for i in prime_checker_range(10**5+1) if prime_checker((i+1)//2)]
di = [0]*(10**5+1)
c = 1
for p in range(len(ls)):
    if p != len(ls)-1:
        for m in range(ls[p],ls[p+1]):
            di[m] = c
    else:
        for m in range(ls[p],10**5+1):
            di[m] = c
    c += 1
for k in range(q):
    l,r = map(int,input().split())
    print(di[r]-di[l-1])



