paint = list(map(int,input().split()))
cnt = {}

for c in paint:
    cnt.setdefault(c,0)
    cnt[c] += 1
    
print(len(cnt))