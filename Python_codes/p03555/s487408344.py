c = []
c.append(list(input()))
c.append(list(input()))
if c[0][0] == c[1][2] and c[0][2] == c[1][0] and c[1][1] == c[0][1]:
    print("YES")
else:
    print("NO")