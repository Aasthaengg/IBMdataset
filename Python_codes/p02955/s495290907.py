n,k = map(int,input().split())
a = list(map(int,input().split()))

sum_a = sum(a)
divisors = []
for i in range(1,int(sum_a**0.5)+1):
    if sum_a % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(sum_a//i)

divisors.sort(reverse=True)

for i in range(len(divisors)):
    b = [0]*n
    for j in range(n):
        b[j] = a[j] % divisors[i]
    b.sort(reverse=True)
    plus = sum(b)
    minus = 0
    for j in range(n):
        if plus == minus:
            break
        else:
            plus -= b[j]
            minus += (divisors[i] - b[j])
    if plus <= k:
        print(divisors[i])
        break
