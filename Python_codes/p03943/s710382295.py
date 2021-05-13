import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限
a = list(map(int,input().split()))
for i in range(1,(2**3)-1):
    distribution = [0,0]
    
    for j in range(3):
        distribution[(i>>j)&1]+= a[j]
    if distribution[0] == distribution[1]:
        break
if distribution[0] == distribution[1]:
    print("Yes")
else:
    print("No")
