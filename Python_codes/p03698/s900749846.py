S = input()

for s in S:
  if S.count(s) != 1:
    print("no")
    exit()
    
print("yes")