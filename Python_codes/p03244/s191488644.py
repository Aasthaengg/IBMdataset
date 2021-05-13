import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Vs = list(mapint())

even = []
odd = []
for i in range(N):
    if i%2==1:
        even.append(Vs[i])
    else:
        odd.append(Vs[i])

from collections import Counter
ceven = Counter(even)
ans = 0
even_second = 0
for i, (num, cnt) in enumerate(ceven.most_common()):
    if i==0:
        even_most = cnt
        even_num = num
    if i==1:
        even_second = cnt
    ans += cnt
codd = Counter(odd)
odd_second = 0
for i, (num, cnt) in enumerate(codd.most_common()):
    if i==0:
        odd_most = cnt
        odd_num = num
    if i==1:
        odd_second = cnt
    ans += cnt

if even_num==odd_num:
    ans = min(ans-odd_most-even_second, ans-odd_second-even_most)
else:
    ans -= odd_most+even_most
print(ans)