s=input()
key="keyence"
li=[]
for i in range(len(key)):
  li.append([key[:i],key[i:]])
  
for i in li:
  #print("{} {}".format(s[:len(i[0])],s[-len(i[1]):]))
  if s[:len(i[0])]==i[0] and s[-len(i[1]):]==i[1]:
    print("YES")
    break
else:
  print("NO")
