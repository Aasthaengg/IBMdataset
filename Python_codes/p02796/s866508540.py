n = int(input())
 
lines = []
for i in range(n):
  x,l = map(int,input().split())
  lines.append([x-l,x+l])
lines = sorted(lines,key=lambda x:x[1])
count = 0
kari = -9999999999999
for i in range(n):
  if lines[i][0] >= kari:
    count += 1
    kari = lines[i][1]
print(count)