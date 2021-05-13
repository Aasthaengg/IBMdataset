n, m, x, y = map(int, input().split())
Xn = list(map(int, input().split()))
Yn = list(map(int, input().split()))

Z = []
for z in range(x+1, y+1):
#    print(z)
    if max(Xn) < z and z <= min(Yn):
        Z.append(z)
        print('No War')
        break
else:
    print('War')