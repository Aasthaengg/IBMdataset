N = int(input())

# 約数列挙(1,N)も含まれる
prime, i = set(), 1
while i * i <= N:
    if N % i == 0:
        prime.add(i)
        prime.add(N//i)
    i += 1

#print(prime)
ans = []
for i in prime:
    if i == 1:
        continue
    i -= 1
    if N // i == N % i:
        ans.append(i)

print(sum(ans))
