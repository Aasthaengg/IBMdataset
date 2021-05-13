from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
cd = Counter(D)
ct = Counter(T)

for k, v in ct.items():
  if cd[k] < v:
    print('NO')
    exit()
    
print('YES')