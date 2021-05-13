#ITP1_11-A Dice 1
rep={
    "N":[4,0,2,3,5,1],
    "S":[1,5,2,3,0,4],
    "E":[2,1,5,0,4,3],
    "W":[3,1,0,5,4,2]
}

d = input().split(" ")
NSEW = input()
c=[d]
for i in range(len(NSEW)):
    c.append([0,0,0,0,0,0])

for i in range(len(NSEW)):
    r=rep[NSEW[i]]
    for j in range(6):
        c[i+1][r[j]]=c[i][j]
print(c[len(NSEW)][0])