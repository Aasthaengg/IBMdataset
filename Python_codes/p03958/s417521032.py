K,T = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=True)

if T == 1:
    print(A[0]-1)
    exit()
su = sum(A[1:])
if A[0] - su >= 2:
    print(A[0] - su - 1)
else:
    print(0)