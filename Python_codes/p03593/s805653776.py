from collections import Counter
H, W = map(int, input().split())
D = []
for _ in range(H):
    D.extend(list([v for v in input()]))
C = Counter(D)
L = list([v for i, v in C.most_common()])

g1 = sum(v % 2 for v in L)
g4 = sum(v//4 for v in L)

if g4 >= (W-(W % 2))*(H-(H % 2))//4 and g1 == H & 1 & W:
    print("Yes")
else:
    print("No")
