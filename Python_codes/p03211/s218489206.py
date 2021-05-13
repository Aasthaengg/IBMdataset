s=input()
x=len(s)-2
l=[]
for i in range(x):
    l.append(abs(int(s[i:i+3])-753))
y=l.index(min(l))

print(abs(int(s[y:y+3])-753))