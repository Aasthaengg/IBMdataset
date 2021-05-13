v = list(input().split(' '))

if v[0][len(v[0])-1] == v[1][0] and v[1][len(v[1])-1] == v[2][0]:
        print("YES")
else:
        print("NO")