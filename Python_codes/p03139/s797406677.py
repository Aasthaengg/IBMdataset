N, A, B = map(int, input().split())

r_max = min(A, B)
if A + B > N:
    r_min = A + B - N
else:
    r_min = 0

print(r_max, r_min)