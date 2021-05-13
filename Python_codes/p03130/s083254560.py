a = [0] * 4
for i in range(3) :
  x, y = map(int, input().split())
  a[x-1] = a[x-1] + 1
  a[y-1] = a[y-1] + 1
if a[0] ^ a[1] ^ a[2] ^ a[3] == 0 : print("YES")
else : print("NO")