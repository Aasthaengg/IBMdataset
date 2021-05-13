N = int(input())
a = list(map(int,input().split()))
n = 1
ans = 0
for i in a:
    if i != n:
        ans += 1
    else:
        n +=1
if n == 1:
    print("-1")
else:
    print(ans)