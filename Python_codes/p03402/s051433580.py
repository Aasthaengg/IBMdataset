A,B = map(int,input().split())

H,W = 100,100
D = [["."]*100 for _ in [0]*50]+[["#"]*100 for _ in [0]*50]

c = 1
i = 1
j = 1
while c<B:
    D[i][j] = "#"
    c += 1
    j += 2
    if j>100:
        j-=100
        i+=2
c = 1
i = 51
j = 1
while c<A:
    D[i][j] = "."
    c += 1
    j += 2
    if j>100:
        j-=100
        i+=2

print(H,W)
for out in D:
    print("".join(out))