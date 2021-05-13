a,b,c,d = input().split()

aa = int(a)*int(c)
bb = int(a)*int(d)
cc = int(b)*int(c)
dd = int(b)*int(d)

li = [aa,bb,cc,dd]

print(max(li))