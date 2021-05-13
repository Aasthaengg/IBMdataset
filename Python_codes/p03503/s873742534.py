N=int(input())
F=[int('0b'+''.join(list(input().split(' '))),0) for i in range(N)]
P=[list(map(int,input().split(' '))) for i in range(N)]
ans = -float('inf')
for i in range(1,1024):
    tmp = 0
    for j,k in zip(P,F):
        tmp += j[str(bin(i&k)).count('1')]
    ans = max(tmp,ans)
print(ans)