N = int(input())
a = [int(i) for i in input().split()]

color = []
color2 = []

def rate(a):
    if a < 400:
        if 1 not in color:
            color.append(1)
    elif 400<= a and a<800:
        if 2 not in color:
            color.append(2)
    elif 800<=a and a<1200:
        if 3 not in color:
            color.append(3)
    elif 1200<=a and a<1600:
        if 4 not in color:
            color.append(4)
    elif 1600<=a and a<2000:
        if 5 not in color:
            color.append(5)
    elif 2000 <=a and a<2400:
        if 6 not in color:
            color.append(6)
    elif 2400 <=a and a<2800:
        if 7 not in color:
            color.append(7)
    elif 2800<=a and a<3200:
        if 8 not in color:
            color.append(8)
    elif a>= 3200:
        color2.append(a)

for i in range(N):
    rate(a[i])

max = len(color) + len(color2)

if len(color) == 0:
    print(1,max)
else:
    print(len(color),max)