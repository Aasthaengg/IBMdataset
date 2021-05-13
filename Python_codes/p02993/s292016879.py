x = input ()
a = 'Good'
for i in range (3):
  if x[i] == x[i+1]:
    a = 'Bad'
    break
print (a)