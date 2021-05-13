N = int(input())
L = list(map(int, input().split()))
S = 0
for i in L:
  S += int(i)
print('YES' if S%2 == 0 else 'NO')