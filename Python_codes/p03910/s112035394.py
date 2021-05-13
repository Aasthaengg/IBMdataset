n = int(input())

i = 1
l = [1]
while n >= (i+1)*i//2:
    i += 1
    l.append(i)

l.remove((i+1)*i//2-n)

for j in l:
    print(j)