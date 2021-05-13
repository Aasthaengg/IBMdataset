l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
    
l.sort()
print(l[2] * 10 + l[1] + l[0])