n = int(raw_input())

R = [0 for i in range(n)]

ans = 1 - 10**9
for i in range(n):
    R[i] = int(raw_input())
    if i == 0:
        min_R = R[0]
        continue
    if min_R < R[i]:
        if ans < R[i]-min_R:
            ans = R[i] - min_R
    elif min_R > R[i]:
        if ans < R[i]-min_R:
            ans = R[i] - min_R
        min_R = R[i]
    else:
        if ans < 0:
            ans = 0
        
print ans