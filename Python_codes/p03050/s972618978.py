def prime(p):
    memo = [p]
    for i in range(2,(int(p**0.5)+1)):
        if p%i == 0:
            memo.append(i)
            memo.append(p//i)
    return memo

x = int(input())

if x== 1:
    print(0)
    exit()

memo = prime(x)

ans = 0

for i in memo:
    if x%(i-1)==x//(i-1):
        ans += i-1
print(ans)