from itertools import combinations
initials = {'M':0,'A':0,'R':0,'C':0,'H':0}
for _ in range(int(input())):
  name = input()
  initials[name[0]] = initials.get(name[0],0)+1
answer = 0
for initial in combinations('MARCH',3):
  answer += initials[initial[0]]*initials[initial[1]]*initials[initial[2]]
print(answer)