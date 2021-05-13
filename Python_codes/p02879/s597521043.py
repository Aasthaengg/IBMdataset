a,b = map(int,input().split())

if a <=9 and b <=9:
    print(a * b)

elif a >=10 or b >=10:
    print('-1')