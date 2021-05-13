from collections import Counter
 
N = int(input())
S = list(input())
c = Counter(S)
left_facing_west = 0
right_facing_east = c['E']
ans = float('inf')
for s in S:
    if s == 'W':
        ans = min(ans,left_facing_west+right_facing_east)
        left_facing_west += 1
    else:
        right_facing_east -= 1
        ans = min(ans,left_facing_west+right_facing_east)
print(ans)