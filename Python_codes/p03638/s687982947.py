h,w = map(int, input().split())
n = int(input())
a = list(map(int, input().split( )))
ans = []

for i in range(n):
    for _ in range(a[i]):
        ans.append(i+1)
for i in range(h):
    if not i%2:
        print(*ans[w*i:w*i+w])
    else:
        print(*ans[w*i+w-1:w*i-1:-1])
        

