n, m = map(int, input().split())

a = []
b = list((0 for i in range(m)))

for i in range(n):
    a.append(list(map(int, input().split())))
    
for a_ in a:
    k = a_[0]
    for k_ in range(k):
        b[(a_[k_ + 1]) - 1] += 1
        
ans = 0
for b_ in b:
    if b_ == n:
        ans += 1
print(ans)