n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
ans = [0]*3

for i in range(n):
    if p[i] <= a:
        ans[0] += 1
    elif p[i] <= b:
        ans[1] += 1
    else:
        ans[2] += 1

print(min(ans[0],ans[1],ans[2]))