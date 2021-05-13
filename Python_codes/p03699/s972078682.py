N = int(input())
S = [int(input()) for _ in range(N)]

mn = 200
for i in range(N):
    if S[i] % 10 != 0:
        if S[i] <= mn:
            mn = S[i]
total = sum(S)
if total % 10 != 0:
    print(total)
elif mn == 200:
    print(0) 
else:
    print(total - mn)