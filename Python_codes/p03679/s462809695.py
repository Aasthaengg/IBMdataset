x,a,b = map(int,(input().split())) 

hantei = b - a

if hantei <= 0:
    print("delicious")
elif x >= hantei:
    print("safe")
elif (x + 1) <= hantei:
    print("dangerous")