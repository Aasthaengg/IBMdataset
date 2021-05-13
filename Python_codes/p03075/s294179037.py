from itertools import combinations
L  = []
for i in range(5):
    L.append(int(input()))
k = int(input())
for i,j in combinations(L,2):
    if abs(i-j) > k:
        print(":(")
        break
else:
    print("Yay!")