N,K = map(int,input().split())
A = list(map(int,input().split()))

def f(x):
    ret = 0
    for i in range(N):
        ret += A[i] ^ x
    return ret

###2**(num-1)<=K<2**numなるnumを求める
P = bin(K)
num = len(list(map(int,P[2:])))

best = 0

for i in range(num):
    count = 0###2**iの位が1になるAの個数
    for j in range(N):
        if A[j] > A[j]^(2**i):
            count += 1
    
    if count <= N - count:
        best += 2**i

#print(best)
can = [0]*40

for i in range(40):
    if K & 2**i == 0:
        continue
    for j in range(0,i):
        can[i] += best & 2**j
    for j in range(i+1,40):
        can[i] += K & 2**j

can.append(K)

print(max(list(map(f,can))))