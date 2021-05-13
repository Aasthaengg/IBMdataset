n = int(input())
l = []
c = 0
for i in range(1,n+1,2):
    c = 0
    for j in range(1,i+1,2):
        if i%j == 0 :
            c += 1
    if c == 8 :
        l.append(i)
print(len(l))
