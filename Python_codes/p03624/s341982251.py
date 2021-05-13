s = input ()
x = 0
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range (len(l)):
  if s.count(l[i]) == 0:
    print (l[i])
    x = 1
    break
if x == 0:
  print ('None')