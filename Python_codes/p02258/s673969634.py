n = int(input())
R_max = -10**9
R_min = int(input())
for i in range(n-1):
    R = int(input())
    if R_max < R - R_min:
        R_max = R - R_min

    if R < R_min:
        R_min = R

print(R_max)