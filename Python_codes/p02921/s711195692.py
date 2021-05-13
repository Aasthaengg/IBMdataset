S = input()
T = input()

r = 0
for s,t in zip(S,T):
  r += 1 if s == t else 0
print(r)