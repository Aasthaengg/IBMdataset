a = list(input())

l = []
for i in zip(a, a[1:]):
    l.append(i)

if any([l[i][0] == l[i][1] for i in range(3)]):
    print('Bad')
else:
    print('Good')

