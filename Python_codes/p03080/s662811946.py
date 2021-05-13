n = int(input())
s=input()

red=0
for i in s:
    if i=='R':
        red+=1

if red>n-red: print('Yes')
else: print('No')