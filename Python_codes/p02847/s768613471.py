A = input()

S = ['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(7):
  if A == S[i]:
    print(7-i)
    break
  i+=1
