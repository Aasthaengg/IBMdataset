from bisect import *
N = int(input())
T, A = map(int, input().split())
H = []
for i, h in enumerate(map(int, input().split())):
    H.append((T-h*0.006, i))
H.sort()
H2 = [h for h, _ in H]
i = bisect_left(H2,A)
if i==N:
    print(H[-1][1]+1)
elif abs(H[i-1][0]-A) > abs(H[i][0]-A):
    print(H[i][1]+1)
else:
    print(H[i-1][1]+1)