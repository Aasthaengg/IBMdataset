import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))

for i in range(len(l)):
    l[i] = i - l[i] + 1

l.sort()
t = l[int(len(l) / 2)]

for i in range(len(l)):
    l[i] = abs(l[i] - t)
    
print(sum(l))