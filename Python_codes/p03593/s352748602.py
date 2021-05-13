from collections import defaultdict

H, W = map(int, input().split())
cnt = defaultdict(int)

for _ in range(H):
    a = list(input())
    
    for ai in a:
        cnt[ai] += 1

four = 0
odd = 0

for v in cnt.values():
    four += v//4
    odd += v%2
    
if four>=H//2*(W//2) and odd<=1:
    print('Yes')
else:
    print('No')