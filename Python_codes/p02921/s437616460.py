S = input()
T = input()
x = 0
y = list(range(3))
for i in y:
 if S[i] == T[i]:
   x = x + 1

print(x)