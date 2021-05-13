import collections

N = int(input())
lan = ["".join(sorted(input())) for n in range(N)]
#print(lan)
lans = collections.Counter(lan)
#print(lans)
ans = 0
for si in set(lan):
    n = lans[si]
    ans += n * (n - 1) // 2
print(ans) 
