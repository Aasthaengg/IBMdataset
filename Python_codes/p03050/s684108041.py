n=int(input())

def divisore(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

d=divisore(n)

ans=0
for i in d[1:]:
  cand=i-1
  if n//cand==n%cand:
    ans+=cand

print(ans)