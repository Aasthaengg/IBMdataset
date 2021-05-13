a , b , c = map(int, input().split())
fnl = b
a+=1
 
if c < b:
    fnl+=c
else:
    fnl += b
    fnl += min(c-b,a)
print(fnl)