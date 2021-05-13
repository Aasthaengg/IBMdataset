A,B,C = map (int, input ().split ())
if A>=B>=C or A>=C>=B:
  print (B+C)
elif B>=A>=C or B>=C>=A:
  print (A+C)
else:
  print (A+B)