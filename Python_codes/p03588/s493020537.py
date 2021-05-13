import sys
readline=sys.stdin.readline
read=sys.stdin.read

n=int(readline())
p=[list(map(int,lst.split())) for lst in read().splitlines()]
e=max(p, key=lambda x:x[0])
print(e[0]+e[1])