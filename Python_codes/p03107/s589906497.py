s=[int(x) for x in list(input())]
x=s.count(0)
print(min(x,len(s)-x)*2)