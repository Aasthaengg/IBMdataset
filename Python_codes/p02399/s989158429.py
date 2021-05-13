s = input().split(" ")
a = int(s[0])
b = int(s[1])
d = int(a / b)
r = a % b
f = round((a / b),7)
print("{0} {1} {2}".format(d,r,f))