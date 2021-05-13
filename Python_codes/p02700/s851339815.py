a,b,c,d = map(int, input().split())

for i in range(100):
    c -= b
#    print('c', c)
    if c < 1:
        print('Yes')
        break

    a -= d
 #   print('a',a)
    if a < 1:
        print('No')
        break
