from collections import Counter
n = int(input())
l = [''.join(sorted(input())) for i in range(n)]
    
c = Counter(l)
cnt = 0
for val in c.values():
    cnt += val * (val-1) //2

print(cnt)