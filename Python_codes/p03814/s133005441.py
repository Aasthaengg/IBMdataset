s=input()
num1=[]
num2=[]
for i in range(len(s)):
    if s[i]=="A":
        num1.append(i)
    elif s[i]=="Z":
        num2.append(i)

print(max(num2)-min(num1)+1)
