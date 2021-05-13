import collections
N = int(input())
D = list(map(int, input().split()))
DC = collections.Counter(D)
M = int(input())
T = list(map(int, input().split()))
TC = collections.Counter(T)

for num, count in TC.items():
     if DC[num] < count:
         print('NO')
         exit()
print('YES')
