n = int(input())
vn = [int(num) for num in input().split()]

while(len(vn) >= 2):
  vn.sort()
  f = vn.pop(0)
  s = vn.pop(0)
  vn.append((f+s)/2.0)

print(vn[0])