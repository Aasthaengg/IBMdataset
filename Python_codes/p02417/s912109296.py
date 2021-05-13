import sys
s=str()
x="abcdefghijklmnopqrstuvwxyz"
for a in sys.stdin:s+=a.lower()
for c in x:print(c+" : "+str(s.count(c)))