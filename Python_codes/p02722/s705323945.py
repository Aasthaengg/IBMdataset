n=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

tmp=make_divisors(n-1)
tmp.remove(1)
ans=set(tmp)
cnt=make_divisors(n)
cnt.remove(1)
for i in range(len(cnt)):
    k=cnt[i]
    gh=n
    while(gh%k==0):
        gh//=k
    if gh%k==1:
        ans.add(k)

print(len(ans))