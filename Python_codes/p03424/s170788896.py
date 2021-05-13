N = int (input ())
S = input ().split ()
x = 'Three'
for i in range (N):
  if S[i] == 'Y':
    x = 'Four'
    break
print (x)