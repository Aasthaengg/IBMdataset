a = input()
a = int(a)
h = a//3600
m = a%3600//60
s = a%60
print(str(h)+":"+str(m)+":"+str(s))

