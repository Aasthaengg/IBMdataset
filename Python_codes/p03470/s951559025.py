n = int(input())
c = set()
for i in range(n):
  c |= {int(input())}
print(len(c))