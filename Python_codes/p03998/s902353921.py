A = input() + "x"
B = input() + "x"
C = input() + "x"

a=b=c=0

x = 'a'
ans = ""
while x!='x':
  if x=='a':
    x = A[a]
    a += 1
    ans = "A"
  elif x=='b':
    x = B[b]
    b += 1
    ans = "B"
  elif x=='c':
    x = C[c]
    c += 1
    ans = "C"

  # print(a,b,c)

print(ans)
