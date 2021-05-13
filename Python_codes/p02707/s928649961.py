n = int(input())
l = [0 for x in range(n)]
for i in list(map(int,input().split())):
  l[i-1] += 1
print(*l, sep='\n')