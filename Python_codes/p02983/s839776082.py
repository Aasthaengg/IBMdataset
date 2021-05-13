l, r = map(int, input().split())
if r - l >= 2019:
    print(0)
    exit()

l = l%2019
r = r%2019

if l >= r:
    print(0)
else:
    ans = float('inf')
    for left in range(l, r):
        for right in range(left+1, r+1):
            ans = min(ans, (left*right)%2019)
    print(ans)