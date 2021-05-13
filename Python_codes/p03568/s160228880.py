n = int(input())
a = list(map(int,input().split()))
ans = 3**n
res = 1
for x in a:
    if x%2:res*=1
    else:res*=2
print(ans-res)