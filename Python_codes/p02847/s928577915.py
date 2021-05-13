youbi=['MON','TUE','WED','THU','FRI','SAT','SUN']
s=input()
for i in range(len(youbi)):
  if s=='SUN':
    print(7)
    exit()
    
  elif youbi[i]==s:
    print(6-i)