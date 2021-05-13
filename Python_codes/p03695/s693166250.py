N = int(input())
A=list(map(int, input().split()))
ls = [0]*9
for i in range(N):
    if 1 <= A[i] <= 399:
        ls[0] += 1
    elif 400 <= A[i] <= 799:
        ls[1] += 1
    elif 800 <= A[i] <= 1199:
        ls[2] += 1
    elif 1200 <= A[i] <= 1599:
        ls[3] += 1
    elif 1600 <= A[i] <= 1999:
        ls[4] += 1
    elif 2000 <= A[i] <= 2399:
        ls[5] += 1
    elif 2400 <= A[i] <= 2799:
        ls[6] += 1
    elif 2800 <= A[i] <= 3199:
        ls[7] += 1
    else:
        ls[8] += 1
c = 0
for i in range(8):
    if ls[i]:
        c += 1
m = c if c > 0 else int(ls[-1]>0)
M = c + ls[-1]
print(m, M)