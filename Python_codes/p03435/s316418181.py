c = [list(map(int, input().split())) for i in range(3)]
print("Yes" if c[1][0]-c[0][0]==c[1][1]-c[0][1]==c[1][2]-c[0][2] and c[2][0]-c[0][0]==c[2][1]-c[0][1]==c[2][2]-c[0][2]
     else "No")