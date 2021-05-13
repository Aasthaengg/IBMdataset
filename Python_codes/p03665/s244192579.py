def combination(n,r=-1):
    #res[r] = nPr
    if r==-1:
        r = n
    #nCrの一覧を返す。rの上限も 
    if (r<0) or (n<r):
        return 0
    cur = 1
    res = []
    res.append(cur)
    for i in range(1,r+1):
        cur *= n + 1 -i
        cur //= i
        res.append(cur)
    return res
N,P = [int(hoge) for hoge in input().split()]
A = sum([int(hoge)%2 for hoge in input().split()])
B = N - A#偶数
C = combination(A)
comb = 0
for i in range(P,A+1,2):
    comb += C[i]
print(2**B * comb)