A,B,C = map(int,input().split())

water = ((B + C) - A)
if water < 0 :
    print(0)
else:
    print(water)