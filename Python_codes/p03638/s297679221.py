h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))
hw = [[] for i in range(h)]
ans = []
for i in range(n):
    for j in range(a[i]):
        ans.append(i+1)
for i in range(h):
    if i % 2 == 0:
        print(*ans[w*i:w*(i+1)])
    else:
        print(*ans[w*(i+1)-1:w*i-1:-1])