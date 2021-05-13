N = int(input())
a = [0]*N
b = [0]*N
for i in range(N):
    P = int(input()) - 1
    a[i] = P
    b[P] = i
c = 1
m = 1
for i in range(1,N):
    if b[i] > b[i-1]:
        c += 1
        if c > m:
            m = c
    else:
        c = 1
print(N-m)