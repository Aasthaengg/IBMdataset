a = []
while True:
    x = input()
    if x == 0:
        break
    a.append(x)

for i,v in enumerate(a):
    print "Case "+str(i+1)+": " + str(v)