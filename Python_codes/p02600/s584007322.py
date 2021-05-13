x=int(input())
a=400
for i in range(8,0,-1):
    if a<=x<a+200:
        print(i)
        exit()
    a+=200
