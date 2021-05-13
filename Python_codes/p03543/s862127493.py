N = list(input())

c = 1
p = N[0]
for i in range(1,len(N)):
    if p == N[i]:
        c += 1
    else:
        p = N[i]
        c = 1
    if c >= 3:
        print('Yes')
        exit()

print('No')
