n=[]
while 1:
    num=raw_input()
    if num=="0":
        break
    else :
        n.append(num)
for i in xrange(len(n)):
    print("Case "+str(i+1)+": "+n[i])