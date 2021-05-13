s=input()
l=["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(s)):
  try:
    l.remove(s[i])
  except:
    continue
try:
  print(l[0])
except:
  print("None")