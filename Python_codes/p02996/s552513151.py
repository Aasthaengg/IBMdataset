import sys
input = sys.stdin.readline

n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([b, a])

ab.sort()

time = 0

for b, a in ab:
    time += a
    if b < time:
        print('No')
        exit()
    
print('Yes')

