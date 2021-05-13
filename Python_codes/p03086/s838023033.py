S = input()
ans = 0
lsATCG = ['A','T','C','G']
count = 0
for s in S:
    if s in lsATCG:
        count += 1
    else:
        ans = max(ans,count)
        count = 0
ans = max(ans,count)
print(ans)