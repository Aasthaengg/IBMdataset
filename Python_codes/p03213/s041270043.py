def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1: table.append(n)
    return table

n = int(input())
d = [0]*(n+1)
for i in range(2, n+1):
    for j in prime_decomposition(i):
        d[j] += 1
d.sort(reverse=True)
nums = [0]*5
for i in d:
    if i >= 74: j = 5
    elif i >= 24: j = 4
    elif i >= 14: j = 3
    elif i >= 4: j = 2
    elif i >= 2: j = 1
    else: j = 0
    for k in range(j):
        nums[4-k] += 1
print(nums[0]+(nums[1]*(nums[4]-1)+(nums[2]*(nums[3]-1))+nums[3]*(nums[3]-1)*(nums[4]-2)//2))