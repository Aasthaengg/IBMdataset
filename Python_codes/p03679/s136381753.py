x, buy, eat = map(int,input().split())

if buy >= eat:
    print("delicious")
elif eat-buy <= x:
    print("safe")
elif eat - buy > x:
    print("dangerous")