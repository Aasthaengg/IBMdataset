#Beginning
N1, N2, N3, N4 = map(int, input().split())
L = [N1,N2,N3,N4]
L.sort()
if L == [1,4,7,9]:
    print("YES")
else:
    print("NO")