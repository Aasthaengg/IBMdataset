N = int(input())
A = []
B = []
cnt = 0
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(N)[::-1]:
    amari = (A[i] + cnt) % B[i]
    if amari != 0:
        add = B[i] - amari
        cnt += add
print(cnt)    