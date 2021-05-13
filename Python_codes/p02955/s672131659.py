n,k = map(int,input().split())
a = list(map(int,input().split()))

sum1 = sum(a)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

li = make_divisors(sum1)

ans = 0

for i in li:
    b = sorted(list(map(lambda x: x % i,a)))
    count = 0
    flag = -1
    for j in range(len(b)):
        if b[j] % i != 0:
            count += b[j]
            while b[j] > 0:
                if b[j] + b[flag] < i:
                    b[flag] += b[j]
                    b[j] = 0
                else:
                    b[j] -= i - b[flag]
                    b[flag] = i
                    flag -= 1
    if count <= k:
        ans = max(ans,i)
print(ans)
