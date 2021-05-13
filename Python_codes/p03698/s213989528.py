s = input()
n = [0]*26
for e in s:
  n[ord(e)-ord('a')]+=1
for i in n:
  if i>1:
    print("no")
    exit()
print("yes")
