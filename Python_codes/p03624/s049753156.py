s=input()
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(26):
  if al[i] not in s:
    print(al[i])
    exit()
print('None')