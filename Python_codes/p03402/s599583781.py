A, B = map(int,input().split())

S = [["."]*100 for i in range(100)]

for i in range(50,100):
    for j in range(0,100):
        S[i][j] = "#"

for i in range(B-1):
    S[2*(i//50)][(i%50)*2+(i//50)%2] = "#"
for i in range(A-1):
    S[2*(i//50)+51][(i%50)*2+(i//50)%2] = "."

print(100,100)
for i in range(100):
    print("".join(S[i]))
