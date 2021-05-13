N = int(input())

def digit_sum(a, b):
    ab_sum = 0
    for i in range(1, len(str(a))+1):
        ab_sum += a % 10
        a = a // 10
    
    for i in range(1, len(str(b))+1):
        ab_sum += b % 10
        b = b // 10
    
    return ab_sum

min_sum = float("inf")
for i in range(1, (N//2)+1):
    a = i
    b = N - i
    if digit_sum(a, b) < min_sum:
        min_sum = digit_sum(a, b)

print(min_sum)