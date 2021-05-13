l=[]
for i in range(int(input())):
    l.append(int(input()))
print(sum(l)-max(l)//2)