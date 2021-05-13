A,B,K = map(int,input().split())
lsans = []
for i in range(A,A+K):
    if i <= B:
        lsans.append(i)
for j in range(B+1-K,B+1):
    if j >= A and not(j in lsans):
        lsans.append(j)
for i in lsans:
    print(i)