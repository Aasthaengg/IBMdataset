from collections import Counter
n = int(input())
a,b,c = [input() for _ in range(3)]

ans = 0
for x,y,z in zip(a,b,c):
    c = Counter([x,y,z])
    ans += 3 - c.most_common()[0][-1]
        
print(ans)
