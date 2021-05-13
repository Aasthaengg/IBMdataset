a,b,c,d = map(int, input().split())

x = c-a
y = d-b

print(str(c-y)+" "+str(d+x)+" "+str(a-y)+" "+str(b+x))