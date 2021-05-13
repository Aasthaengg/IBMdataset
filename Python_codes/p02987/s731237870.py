string = input()
a,b,c,d = string[0],string[1],string[2],string[3]

def truth(x):
  count = 0
  if a ==b or a==c or a==d:
    count += 1
  if b ==c or b==d:
    count += 1
  if c ==d:
    count += 1
  if a == b == c or a ==b ==d or a==c==d:
    return False
  return count>1

if truth(a): print("Yes")
else: print("No")
                   
