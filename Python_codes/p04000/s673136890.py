h, w, n = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(2):
        A[i][j] -= 1

D = {}

for i in range(n):
    # print(D)
    for j in range(-1, 2):
        for k in range(-1, 2):
            if 1 <= A[i][0]+j <= h-2 and 1 <= A[i][1]+k <= w-2:
                try:
                    D[(A[i][0]+j, A[i][1]+k)] += 1
                except:
                    D[(A[i][0]+j, A[i][1]+k)] = 1

ANS = [0] * 10
for i in D.values():
    ANS[i] += 1
ANS[0] = (h-2) * (w-2) - sum(ANS[1:])

for i in ANS:
    print(i)