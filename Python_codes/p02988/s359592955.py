import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(2,n):
    if max(p[i-2:i+1]) != p[i-1] and min(p[i-2:i+1]) != p[i-1]:
        count += 1
print(count)
