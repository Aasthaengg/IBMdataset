s=input()
List=[]
for i in range(1,len(s)+1):
    if i%2==1:
        List.append(s[i-1])
print("".join(List))