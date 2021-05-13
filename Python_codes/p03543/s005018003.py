N=input()
l=['000','111','222','333','444','555','666','777','888','999']
for i in l:
    if i == N[0:3] or i==N[1:len(N)]:
        print('Yes')
        exit()
print('No')