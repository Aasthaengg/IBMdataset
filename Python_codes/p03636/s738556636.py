s=input()
count=0
for i in range(len(s)):
    if i == 0 or i == len(s)-1:
        continue
    else:  
        count=count+1
r=s[0] + "" + str(count) + "" + s[len(s)-1]

print(r)