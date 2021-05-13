from sys import stdin
def LS(): return list(stdin.readline().rstrip().split())

l = LS()
ans = 0
if l[1] == '+':
    ans = int(l[0])+int(l[2])
else:
    ans = int(l[0])-int(l[2])
    
print(ans)