n=int(input())
d=[int(x) for x in input().split()]
ans=0
import itertools
# (1,2,3),(1,2,4),---,(7,8,9)
for seq in itertools.combinations(range(len(d)),2):
    ans+=d[seq[0]]*d[seq[1]]
print(ans)