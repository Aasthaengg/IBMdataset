h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))

ans = [[0 for i in range(w)] for i in range(h)]

memo = 0
for i in range(len(a)):
    for k in range(a[i]):
        ans[memo//w][memo%w] = i+1
        memo += 1

for i in range(1,len(ans),2):
    ans[i].reverse()


for i in range(h):
    for j in range(w):
        print(ans[i][j]," ",end="")
    print('')




