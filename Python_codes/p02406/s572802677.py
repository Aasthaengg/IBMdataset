n=input()
print "",
for i in range(1, n+1):
  if i%3==0 or str(i)[:-1].find("3")!=-1 or i%10==3:
    print "{}".format(i),