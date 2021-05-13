import itertools
S = str(input())
L = ("+","-")

kouho = list(itertools.product(L, repeat=3))
#print(kouho)
for x in kouho:
  temp = S[0]+x[0]+S[1]+x[1]+S[2]+x[2]+S[3]
  ans = eval(temp)
  if ans == 7:
    print(temp+"=7")
    exit()