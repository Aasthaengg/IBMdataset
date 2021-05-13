import sys
N = int(input())
BA = []
for _ in range(N):
    a, b = map(int, input().split())
    BA.append([b, a])
BA.sort()
time=0
for i in range(N):
    time+=BA[i][1]
    
    if time>BA[i][0]:
        print("No")
        sys.exit()
print("Yes")