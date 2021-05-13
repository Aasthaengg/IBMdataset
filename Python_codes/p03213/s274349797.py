n=int(input())

def prime_fact(x):
    fact=[]
    for i in range(2, int(x**(0.5))+1):
        while x%i==0:
            fact.append(i)
            x//=i
    if x!=1:
        fact.append(x)
    if not fact:
        fact=[x]
    return fact

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
p=eratosthenes(100)
d={}
for p_i in p:
    d[p_i]=0
for i in range(2,n+1):
    pf=prime_fact(i)
    for pf_i in pf:
        d[pf_i]+=1

cnt74=0
cnt24=0
cnt14=0
cnt4=0
cnt2=0

for key in d:
    if d[key]>=74:
        cnt74+=1
    if d[key]>=24:
        cnt24+=1
    if d[key]>=14:
        cnt14+=1
    if d[key]>=4:
        cnt4+=1
    if d[key]>=2:
        cnt2+=1

print(int(cnt74+(cnt2-1)*cnt24+(cnt4-1)*cnt14+(cnt2-2)*cnt4*(cnt4-1)/2))
