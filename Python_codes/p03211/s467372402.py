s=str(input())

l=[]
for i in range(len(s)-2):
    a=abs(int(str(s[i])+str(s[i+1])+str(s[i+2]))-753)
    l.append(a)

print(min(l))