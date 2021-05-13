MM = input()
M = list(MM)
count = 0
for i in M:
  if M.count(i) >1:
    count =1
if count == 0:
  print('yes')
else:
  print('no')