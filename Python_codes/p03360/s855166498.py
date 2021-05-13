A, B, C = map(int, input().split())
K = int(input())
num = max(A,B,C)
for i in range(K):
  num *= 2
print(num+sum([A,B,C])-max(A,B,C))