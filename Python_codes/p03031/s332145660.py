N,M=map(int, input().split())
k=[list(map(int,input().split()))for _ in range(M)]
p=list(map(int,input().split()))
import itertools
import operator
import functools
print(sum(1 for i in itertools.product([True,False],repeat=N)if functools.reduce(operator.and_,[functools.reduce(operator.xor,[i[j-1]for j in k[l][1:]])==p[l]for l in range(M)])))
