from functools import reduce

N = int(input())
A = list(map(int, input().split()))

z = reduce(lambda x,y:x^y, A)
print(*[a^z for a in A], sep=' ')
