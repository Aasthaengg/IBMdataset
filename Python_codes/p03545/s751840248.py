import itertools

s = input()
op = ["+","-"]
for ops in itertools.product(op, repeat=3):
  result = int(s[0]) 
  for i in range(len(ops)):
    if ops[i] == "+":
      result += int(s[i+1]) 
    else :
      result -= int(s[i+1]) 
  if result == 7:
    print(s[0]+ops[0]+s[1]+ops[1]+s[2]+ops[2]+s[3]+"="+str(result))
    break