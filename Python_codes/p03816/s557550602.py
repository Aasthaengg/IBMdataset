N = int(input())
AAA = [int(i) for i in input().split()]
cardlist = [0 for i in range(100010)]
for A in AAA:
    cardlist[A] += 1
for cardnumber, howmany in enumerate(cardlist):
    if howmany>=3:
        if howmany%2==0:
            cardlist[cardnumber]=2
        else:
            cardlist[cardnumber]=1

numof2 = sum([1 for i in cardlist if i==2])

if numof2%2==0:
    print(sum([1 for i in cardlist if i!=0]))
else:
    print(sum([1 for i in cardlist if i!=0])-1)
