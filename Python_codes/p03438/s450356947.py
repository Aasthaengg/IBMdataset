n = int(input())
ai = [int(i) for i in input().split()]
bi = [int(i) for i in input().split()]

sita = 0
ue = 0

for i in range(n):
    if ai[i] >= bi[i]:
        sita += ai[i] - bi[i]
    else:
        ue += (bi[i] - ai[i]+1) // 2

#print(sum(bi),sum(ai),ue,sita)
        
if sum(bi) - sum(ai) - max(ue,sita) >= 0:
    print('Yes')
else:
    print('No')