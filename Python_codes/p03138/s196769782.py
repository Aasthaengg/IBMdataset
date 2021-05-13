N,K = map(int, input().split())
A = list(map(int, input().split()))

keta = len(str(format(K, 'b')))
T = [0]*keta
for a in A:
    for i in range(keta):
        if (((1<<i)&(a))>>i) == 1:
            T[i] += 1

tmp = ''
for t in T:
    if t > N//2:
        tmp += '0'
    else:
        tmp += '1'
XX = list(tmp[::-1])
KK = str(format(K, 'b'))
if int(tmp[::-1], 2) > K:
    for i in range(len(XX)):
        if (XX[i] != KK[i]) and XX[i] == '1':
            XX[i] = '0'
        elif (XX[i] != KK[i]) and XX[i] == '0':
            break

X = int(''.join(XX), 2)
ans = 0
for a in A:
    ans += X^a

print(ans)