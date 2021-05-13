n = int(input())
result = [2]
i = 1
while len(result) < n:
    num = 5*i -1
    for j in range(2, int(pow(num, 0.5))+1):
        while num%j==0:
            num //= j
    if num == 5*i-1:
        result.append(num)
    i += 1
print(*result)