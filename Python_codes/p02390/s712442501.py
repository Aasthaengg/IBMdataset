S = raw_input()
S = int(S)
if S/3600 > 0:
    h = S/3600
else: h = 0
if (S % 3600) / 60 > 0:
    m = (S % 3600) / 60
else: m = 0
if (S % 3600) % 60 > 0:
    s = (S % 3600) % 60
else: s = 0
h= str(h)
m= str(m)
s= str(s)
#print h,m,s
print h + ':' + m + ':' + s