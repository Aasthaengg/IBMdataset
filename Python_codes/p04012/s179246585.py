s=input()
li=[0]*26
for i in range(len(s)):
    li[ord(s[i])-97]+=1
res="Yes"
for i in li:
    if i%2==1:
        res="No"
print(res)