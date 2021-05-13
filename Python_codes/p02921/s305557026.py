sss = input()
ttt = input()

counter = 0
for s, t in zip(sss, ttt):
  if s == t:
    counter += 1
    
print(counter)