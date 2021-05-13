w = list(input())
alp = [chr(i) for i in range(ord('a'), ord('z')+1)]

beautiful = True
for i in alp:
    if w.count(i)%2 != 0:
        beautiful = False
        break
        
if beautiful:
    print('Yes')
else:
    print('No')