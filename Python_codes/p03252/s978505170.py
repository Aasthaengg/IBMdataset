import sys
s = input()
t = input()
dic = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
sl = [0]*26
tl = [0]*26
for i in s: sl[dic[i]] += 1
for i in t: tl[dic[i]] += 1
sl.sort()
tl.sort()
for i in range(26):
    if sl[i] != tl[i]:
        print("No")
        sys.exit()
print("Yes")