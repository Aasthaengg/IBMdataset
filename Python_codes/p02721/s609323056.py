

N,K,C = map(int,input().split())
S = input()

l = [0]*K
r = [0]*K
ld = 0
rd = N-1
for i in range(K) :
    j = K - i - 1
    while S[ld] == 'x' :
        ld += 1
    while S[rd] == 'x' :
        rd -= 1
    l[i] = ld
    ld += 1+C
    r[j] = rd
    rd -= 1+C

for i in range(K) :
    if l[i] == r[i] :
        print(l[i]+1)
