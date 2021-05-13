# coding: utf-8
# Your code here!
s=""
while True:
    try:
        s+=input()
    except:
        break
s=s.lower()
for i in range(ord("a"),ord("z")+1):
    print(chr(i)+" :",s.count(chr(i)))
