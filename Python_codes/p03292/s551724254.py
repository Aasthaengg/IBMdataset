a, b, c = map(int, input().split())
x = [a, b, c]

x.sort()

print(abs(x[0]-x[1])+abs(x[1]-x[2]))