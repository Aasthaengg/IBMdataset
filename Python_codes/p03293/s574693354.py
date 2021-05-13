S=input()
T=input()

def rot(s):
  return s[-1]+s[:-1]

for i in range(len(S)+1):
  if S == T:
    print('Yes')
    exit()
  S = rot(S)
  
print('No')