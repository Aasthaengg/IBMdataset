n = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

divs1 = make_divisors(n - 1)
divs2 = make_divisors(n)
ans = set(divs1[1:])

for kk in divs2[1:]:
    A = n
    while True:
        if A % kk == 0:
            A //= kk
        else:
            break

    if (A - 1) % kk == 0:
        ans.add(kk)

ans.add(n)
print(len(ans))
