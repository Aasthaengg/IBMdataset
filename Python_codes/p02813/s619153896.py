from itertools import permutations
n = int(input())
a,b = [tuple(map(int,input().split())) for _ in range(2)]
s = list(permutations(list(range(1,n+1))))
ans =abs(s.index(b) - s.index(a))
print(ans)