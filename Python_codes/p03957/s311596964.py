f=0
for c in input():
 if c=="C":f=1
 if f&(c=="F"):f=2
print("YNeos"[f!=2::2])