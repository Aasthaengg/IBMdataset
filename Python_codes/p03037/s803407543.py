N, M = map(int, input().split())
 
L = [0] * M
R = [0] * M
for i in range(M):
    L[i], R[i] = map(int, input().split())
 
if max(L) > min(R):
    print("0")
else:
    print(min(R) - max(L) + 1)