from collections import Counter
 
N = int(input())
D = Counter(list(map(int, input().split())))
M = int(input())
T = Counter(list(map(int, input().split())))
 
ans = 'YES'
for key, value in T.items():
    if value > D[key]:
        ans = 'NO'
        break
    else:
        pass
print(ans)