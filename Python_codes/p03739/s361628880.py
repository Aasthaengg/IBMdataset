n = int(input())
A = list(map(int, input().split()))

A_csum = [0] * n
Sum = 0
for i in range(n):
    Sum += A[i]
    A_csum[i] = Sum

pat1 = 0
next_sign = 1
now = 0
for i in range(n):
    if (A_csum[i]+now) * next_sign <= 0:
        diff = next_sign-(A_csum[i]+now)
        pat1 += abs(diff)
        now += diff
    else:
        pass
    next_sign *= -1
    
pat2 = 0
next_sign = -1
now = 0
for i in range(n):
    if (A_csum[i]+now) * next_sign <= 0:
        diff = next_sign-(A_csum[i]+now)
        pat2 += abs(diff)
        now += diff
    else:
        pass
    next_sign *= -1

print(min(pat1,pat2))
    
