import sys
  
l = sys.stdin.readlines()

for i in l[:-1]:
    n = map(int,i.split())
    print(*sorted(n),sep=' ')
