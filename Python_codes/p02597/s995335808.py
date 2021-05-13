n = int(input())
c = input()
p = []
for i in range(n):
  if c[i]=='R':
    p += [i]
print(len([1 for i in p if i>=len(p)]))