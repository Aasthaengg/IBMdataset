s=input()
n=len(s)
ret=0
pos=0
for i in range(n):
    if s[i]=="W":
        ret+=i-pos
        pos+=1
print(ret)