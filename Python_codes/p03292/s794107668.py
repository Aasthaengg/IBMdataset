a,b,c = map(int,input().split())
d = abs(a-b)
e = abs(b-c)
f = abs(c-a)
print(min(d+e,e+f,f+d))

