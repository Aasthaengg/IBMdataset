s = input()
nump = len(s)//2
for i in s:
    if(i=='p'): nump-=1
print(nump)