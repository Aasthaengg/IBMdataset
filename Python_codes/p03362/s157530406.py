N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

cnt = 0
L = []
for i in range(2,55555):
    if i%5==1:
        Ms = make_divisors(i)
        if len(Ms)==2:
            cnt+=1
            L.append(str(i))
    if cnt==55:
        break
print(" ".join(L[0:N]))