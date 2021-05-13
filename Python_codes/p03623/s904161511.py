x,a,b = (int(x) for x in input().split())
print('A' if abs(x-a) < abs(x-b) else "B")