money=int(input())
yen_bills=1000
if yen_bills>=money:
    print(yen_bills-money)
else:
    while yen_bills<money:
        yen_bills+=1000
    print(yen_bills-money)
