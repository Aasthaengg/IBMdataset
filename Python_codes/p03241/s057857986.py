n,m = map(int,input().split())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
li = make_divisors(m) 
#print(make_divisors(m)) [1, 14, 2, 7]
ans = 1
for l in li:
    if l>ans and l*n <= m:
        ans = l
print(ans)