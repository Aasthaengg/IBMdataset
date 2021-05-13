sx, sy, tx, ty = map(int,input().split())

xd = tx - sx
yd = ty - sy

route1 = []
route1.append('R'*xd)
route1.append('U'*yd)

route2 = []
route2.append('L'*xd)
route2.append('D'*yd)

route3 = ['D']
route3.append('R' * (xd + 1))
route3.append('U' * (yd + 1))
route3.append('L')

route4 = ['U']
route4.append('L'*(xd+1))
route4.append('D'*(yd+1))
route4.append('R')

ans = ''.join(route1) + ''.join(route2) + ''.join(route3) + ''.join(route4)
print(ans)


