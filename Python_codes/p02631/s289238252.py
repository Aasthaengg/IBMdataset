n = int(input())
A = list(map(int ,input().split()))
total = 0
for a in A:
  total ^= a
print(*(total ^ a for a in A), sep='\n')