N = list(input())
honlist = ["2","4","5","7","9"]
ponlist = ["0","1","6","8"]
bonlist = ["3"]

if   N[-1] in str(honlist) :
  msg = "hon"
elif N[-1] in str(ponlist) :
  msg = "pon"
else :
  msg = "bon"
  
print(msg)