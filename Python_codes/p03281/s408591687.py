#template
def inputlist(): return [int(j) for j in input().split()]
#template
def divisore(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort(reverse=True)
    return divisors
N = int(input())
ans = 0
for i in range(1,N+1):
    if i % 2 == 0:
        continue
    li = divisore(i)
    if len(li) == 8:
        ans +=1
print(ans)