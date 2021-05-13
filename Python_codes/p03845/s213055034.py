n=int(input())
t=list(map(int, input().strip().split()))
m=int(input())
px = []
for i in range(m):
    array = list(map(int, input().strip().split()))
    px.append(array)
wa=0
for i in range(n):
    wa+=t[i]

for i in range(m):
    print(wa-t[px[i][0]-1]+px[i][1])