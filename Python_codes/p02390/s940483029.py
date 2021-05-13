s=input()
h=int(s/3600)
m=int((int(s)%3600)/60)
s=int(s)%60
print("{0}:{1}:{2}".format(h,m,s))
