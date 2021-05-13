#Beginner 049 B
H, W = map(int, input().split())
p = [input() for i in range(H)]

P = []
for i in range(2*H):
    P.append(p[int(i/2)])

for j in P:
    print(j)
