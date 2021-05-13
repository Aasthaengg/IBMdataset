s = input()
count = 0
for x in range(1,len(s)-1,1):
  count +=1

print(s[0]+str(count)+s[count+1])