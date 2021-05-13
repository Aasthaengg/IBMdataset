S=input()
s_count = len(S)
ans = 0
for i in range(2**(s_count-1)):
  calc_str=""
  for j in range(s_count):
    calc_str = calc_str + S[j]
    if (i>>j) & 1:
      calc_str = calc_str + "+"
  ans = ans + eval(calc_str)
print(ans)