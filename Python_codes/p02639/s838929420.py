ans = 0

a = list(map(int,input().split()))

for idx,val in enumerate(a):
    if val == 0:
        ans = idx + 1

print(ans)