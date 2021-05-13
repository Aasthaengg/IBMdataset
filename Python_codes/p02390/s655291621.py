s=int(raw_input())
a=s/3600
s%=3600
b=s/60
s%=60
print str(a)+":"+str(b)+":"+str(s)