N=int(input())

def primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n+1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

x=primes(N//2+1)
s=[0]*len(x)

for n,i in enumerate(x):
    for j in range(1,7):
        if i**j > N:
            break
        s[n]+=N//(i**j)

c2=0
c4=0
c14=0
c24=0
c74=0
for i in s:
    if i>=2:
        c2+=1
        if i>=4:
            c4+=1
            if i>=14:
                c14+=1
                if i>=24:
                    c24+=1
                    if i>=74:
                        c74+=1
    else:
        break

ans=c4*(c4-1)//2*(c2-2)
ans+=c14*(c4-1)
ans+=c24*(c2-1)
ans+=c74
print(ans)