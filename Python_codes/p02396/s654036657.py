a = []
count = 0
while True:
    a.append(int(input()))
    if a[count] == 0:
        break
    count += 1
for i in range(count):
    print('Case %d'%(i+1)+': %d'%a[i])
