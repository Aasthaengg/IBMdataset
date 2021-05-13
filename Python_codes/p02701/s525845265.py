N = int(input())
s = []
for i in range(N):
  s.append(input())
s_set = set(s)
print(len(s_set))