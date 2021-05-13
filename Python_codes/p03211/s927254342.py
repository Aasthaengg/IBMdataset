s=input()
x=753
a=[]
for i in range(len(s)-2):
  a.append(abs(int(s[i]+s[i+1]+s[i+2])-753))

print(min(a))