n = int(input())

s = []

for x in range(n):
  mozi = input()
  s.append(mozi)
  
new_s = set(s)

print(len(new_s))
