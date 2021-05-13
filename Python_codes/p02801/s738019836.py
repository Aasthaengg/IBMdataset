c=input()
l=[chr(ord('a') + i) for i in range(26)]
a=l.index(c)
print(l[a+1])