N = int(input())
A = input().strip()
B = input().strip()
C = input().strip()
cnt = 0
for i in range(N):
    a = set([A[i],B[i],C[i]])
    if len(a)==3:
        cnt += 2
    elif len(a)==2:
        cnt += 1
print(cnt)