from itertools import combinations
N = int(input())
A = [0 for _ in range(5)]
for _ in range(N):
    a = input().strip()
    if a[0]=="M":
        A[0] += 1
    elif a[0]=="A":
        A[1] += 1
    elif a[0]=="R":
        A[2] += 1
    elif a[0]=="C":
        A[3] += 1
    elif a[0]=="H":
        A[4] += 1
cnt = 0
for x in combinations(range(5),3):
    cnt += A[x[0]]*A[x[1]]*A[x[2]]
print(cnt)