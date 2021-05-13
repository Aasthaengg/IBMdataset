s = open(0).read().rstrip()
 
if len(s)%2:
    s = s[:-1]
else:
    s = s[:-2]
 
while s[:len(s)//2] != s[len(s)//2:]:
    s = s[:-2]
 
print(len(s))