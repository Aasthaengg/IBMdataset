A,B,C,D = input()
for i in range(1<<3):
  S = []
  for j in range(3):
    if 1&(i>>j): 
      S.append("+")
    else: 
      S.append("-")
  if eval(A+S[0]+B+S[1]+C+S[2]+D)==7:
    print(A+S[0]+B+S[1]+C+S[2]+D+"=7")
    exit()