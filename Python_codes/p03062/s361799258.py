N = int(input())
A = list(map(int,input().split()))

A_plus = []
A_zero = []
A_minus = []

a_abs_min = 10**10

for a in A:
    if a > 0:
        A_plus.append(a)
    elif a == 0:
        A_zero.append(a)
    else:
        A_minus.append(a)
        
    if abs(a) < a_abs_min:
        a_abs_min = abs(a)
        
if len(A_minus)%2 == 0:
    ans = sum(A_plus)-sum(A_minus)
else:
    ans = sum(A_plus)-sum(A_minus) - 2*a_abs_min
print(ans)