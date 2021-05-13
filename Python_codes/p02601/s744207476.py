
A,B,C = list(map(int, input().split()))
K = int(input())
for i in range(K):    
    if B >= C:
        C *= 2
    elif A >= B:
        B *= 2
#    print(A,B,C)
if A < B < C:
    print("Yes")
else:
    print("No")
