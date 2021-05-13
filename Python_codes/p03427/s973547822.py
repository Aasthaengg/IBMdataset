n=input()
if n[1:]=='9'*(len(n)-1): print(9*(len(n)-1)+int(n[0]))
else: print(9*(len(n)-1)+int(n[0])-1)