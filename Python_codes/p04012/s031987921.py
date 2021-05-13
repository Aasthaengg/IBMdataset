w = list(input())

w.sort()
c = 1
p = w[0]
for i in range(1,len(w)):
    if p == w[i]:
        c += 1
    else:
        if c%2 == 1:
            print('No')
            exit()
        c = 1
        p = w[i]

if len(w) == 1:
    print('No')
    exit()

print('Yes')
