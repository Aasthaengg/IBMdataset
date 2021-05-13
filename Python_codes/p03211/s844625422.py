n=input()
l=[]
for i in range(len(n)-2):
    l.append(int(n[i:i+3]))
l2=list(map(lambda x: abs(753-x),l))
print(min(l2))