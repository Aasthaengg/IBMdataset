# AGC 025: A – Digits Sum
N = int(input())
n = N // 2 if N % 2 == 0 else N // 2 + 1
min_sum = 9999

for i in range(1, n + 1):
    sum_digits = 0
    A = i
    B = N - i

    while A != 0:
        sum_digits += A % 10
        A //= 10
    
    while B != 0:
        sum_digits += B % 10
        B //= 10
        
    min_sum = min(min_sum, sum_digits)

print(min_sum)