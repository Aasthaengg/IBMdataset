s = input()

for bit in range(1<<3):
  ans=""
  for i in range(3):
    if bit & (1<<i):
      ans+="+"
    else:
      ans+="-"
  ans=s[0]+ans[0]+s[1]+ans[1]+s[2]+ans[2]+s[3]
  if eval(ans)==7:
    print(ans+"=7")
    break