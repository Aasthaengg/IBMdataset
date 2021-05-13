n = int(input().strip())
l = []
 
for i in range(n):
    x, y = map(int, input().split())
    a = y + x
    b = y - x
    l.append([x, y, a, b])
 
la = sorted(l, key=lambda z: z[2])
lb = sorted(l, key=lambda z: z[3])
 
print(max(abs(la[0][0] - la[-1][0]) + abs(la[0][1]-la[-1][1]),
          abs(lb[0][0] - lb[-1][0]) + abs(lb[0][1]-lb[-1][1])
          )
      )