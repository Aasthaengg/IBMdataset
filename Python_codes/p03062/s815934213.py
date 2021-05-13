N = int(input())
A = list(map(int, input().split()))

A_tmp = sorted(A, key=abs, reverse=True,)
total = 0
for i,v in enumerate(A_tmp):
    if (v <= 0) and (i < len(A_tmp)-1):
        A_tmp[i] = (-1) * A_tmp[i]
        A_tmp[i+1] = (-1) * A_tmp[i+1]
        total += A_tmp[i]
    else:
        total += v
print(total)