S=int(raw_input())
h=int(S/3600)
m=(S/60-h*60)
s=(S-h*3600-m*60)
print str(h)+":"+str(m)+":"+str(s)