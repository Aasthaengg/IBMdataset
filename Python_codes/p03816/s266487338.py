from collections import Counter
N = int(input())
A = list(map(int,input().split()))
C = Counter(A)
L = len(C)
print(L-1 if L % 2 == 0 else L)