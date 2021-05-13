N, A, B = map(int, input().split())

sum = 0
for i in range(1, N+1):
    num = i
    val = 0
    while True:
        val += num % 10
        if num // 10 > 0:
            num = num // 10
        else:
            break
    if A <= val <= B:
        sum += i
print(sum)
