N=int(input())

cnt=0
L=[]
def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)

    return divisors

for num in range(2,55555+1):
    l=make_divisors(num)
    if len(l)==2:
        pass
    else:
        continue 
    if num%5==1:
        L.append(num)
        cnt+=1
    if cnt==N:
        break

print(*L)