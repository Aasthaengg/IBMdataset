from itertools import permutations
n = int(input())
p = int(input().replace(' ', ''))
q = int(input().replace(' ', ''))
per = permutations([str(i) for i in range(1, n+1)], n)
lst = []
for pi in per:
  lst.append(int(''.join(pi)))
print(abs(lst.index(p) - lst.index(q)))