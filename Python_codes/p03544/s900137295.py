import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
lis = [2,1]
for i in range(2, n+1):
  lis.append(lis[i-1] + lis[i-2])

print(lis[n])