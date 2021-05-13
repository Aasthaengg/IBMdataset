M = input()
MM = list(M)
count = 0
x = len(MM)
while count == 0:
  if len(MM)%2 ==1:
    MM.pop(-1)
  else:
    a = int(len(MM)/2)
    
    if MM[:a] == MM[a:] and len(MM) != x:
        count =1
    else:
      MM.pop(-1)
print(len(MM))