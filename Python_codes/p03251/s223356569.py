n, m, x, y = map(int, input().split())
xn = [int(num) for num in input().split()]
yn = [int(num) for num in input().split()]

xn.append(x)
yn.append(y)
xn.sort(reverse=True)
yn.sort()
if xn[0] < yn[0]:
  print("No War")
else :
  print("War")
