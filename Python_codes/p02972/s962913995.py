n = int(input())
a = list(map(int, input().split()))

def md(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
b = [0]*n
ans = []
for i in range(n-1,-1,-1):
    if (b[i]%2 != a[i]):
        c = md(i+1)
        ans.append(i+1)
        for j in c:
            b[j-1] += 1
if (b[0]%2!=a[0]):
    print(-1)
else:
    print(len(ans))
    print(*ans)