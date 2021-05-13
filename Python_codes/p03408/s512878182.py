import sys
N = int(input())
array_plus = []
for I in range(N):
    array_plus.append(input())
M = int(input())
array_minus = []
for J in range(M):
    array_minus.append(input())

if not (1 <= N <= 100 and 1 <= M <= 100):
    sys.exit()
for K in range(len(array_plus)):
    if len(array_plus[K]) > 10:
        sys.exit()
    if not array_plus[K].islower():
        sys.exit()
for L in range(len(array_minus)):
    if len(array_minus[L]) > 10:
        sys.exit()
    if not array_minus[L].islower():
        sys.exit()

all = []
all = array_plus+array_minus
all_unique = set(all)
all_unique = list(all_unique)
result = 0
for I in range(len(all_unique)):
    tmp = array_plus.count(all_unique[I]) - array_minus.count(all_unique[I])
    if tmp > result:
        result = tmp
print(result)