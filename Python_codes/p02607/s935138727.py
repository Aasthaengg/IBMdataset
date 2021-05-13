N = int(input())
a = list(map(int,input().split()))
ans = 0
for k,v in enumerate(a):
    if (k+1)%2==1 and v%2==1:
        ans += 1
print(ans)