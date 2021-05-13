N = int(input())
A = list(map(int,input().split()))

gu = []
ans = []

for i in range(N):
    if A[i] % 2 == 0:
        gu.append(A[i])
    else:
        pass

for j in range(len(gu)):
    if gu[j] % 3 == 0 or gu[j] % 5 == 0:
        ans.append(gu[j])
    else:
        pass

if gu == ans:
    print("APPROVED")
else:
    print("DENIED")
