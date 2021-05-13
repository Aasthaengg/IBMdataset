from collections import Counter
n,m = map(int,input().split())
ab_input = [int(j) for i in range(m) for j in input().split()]

ab_count = Counter(ab_input)
if all(v%2==0 for v in ab_count.values()):
    print('YES')
else:
    print('NO')