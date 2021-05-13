S=input()
str = 'abcdefghijklmnopqrstuvwxyz'

for c in str:
    found = False
    for s in S:
       if s == c:
           found = True
           break
    if found:
        continue
    else:
        print(c)
        exit()

print('None')