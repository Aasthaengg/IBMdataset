s = input()
num = 0
for i in range(len(s)):
    if s[i] == 'x':
        num+=1
    
if num >= 8:
    print("NO")
else:
    print("YES")
