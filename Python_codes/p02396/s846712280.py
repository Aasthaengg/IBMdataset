c = 1                                                                       
a = []
while True:
    x = int(input())
    if x == 0:
        break;
    else:
        a = a + [x]

for i in a:
    print('Case {0}: {1}'.format(c,i))
    c += 1