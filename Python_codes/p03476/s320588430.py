q=int(input())
lr = [list(map(int,input().split())) for _ in range(q)]
def primesFactraizar(n):
    is_prime = [True] * (n + 1) #まずは[1]*nを用意
    is_prime[0] = False 
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1): #素数の判定√nまでで十分
        if not is_prime[i]: #非素数は無視
            continue            #continue分はループ中の後続の命令をスキップする
        for j in range(i * 2, n + 1, i): #i*2~nまでのiの倍数を順番に消す
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
primes = primesFactraizar(10**5+1)

cumSum = [0]*(10**5+1)
tmp = 0
for i in range(10**5+1):
    if i in primes and (i+1)//2 in primes:
        tmp += 1 
    cumSum[i] = tmp


for l,r in lr:
    print(cumSum[r]-cumSum[l-1])