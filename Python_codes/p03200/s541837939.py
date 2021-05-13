s=input()
counter=0
res=0
for i in range(len(s)):
    if s[i]=="W":
        counter+=i-res
        res+=1

print(counter)
