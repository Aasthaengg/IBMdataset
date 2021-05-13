

a,b = map(int,input().split())

tower = [1]*999
for i in range(1,999):
  tower[i] = tower[i-1]+i+1

print(tower[b - a - 1] - b)