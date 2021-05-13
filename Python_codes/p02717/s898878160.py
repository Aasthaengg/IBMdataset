n = list(map(int, input().split()))
     
x, y = (n[1], n[0])
n[0], n[1] = (x, y)
     
x, z = (n[2], n[0])
n[0], n[2] = (x, z)
     
print(" ".join(list(map(str, n))))