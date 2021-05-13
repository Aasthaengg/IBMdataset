time=input()
h=time/3600
m=(time%3600)/60
s=(time%3600)%60
print str(h)+':'+str(m)+':'+str(s)