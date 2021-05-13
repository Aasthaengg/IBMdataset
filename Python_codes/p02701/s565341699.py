import sys
input = sys.stdin.readline
N = int(input().rstrip())
lis = {}
for _ in range(N):
  a = input().rstrip()
  if a in lis:
    lis[a] += 1
  else:
    lis[a] = 1
print(len(lis))