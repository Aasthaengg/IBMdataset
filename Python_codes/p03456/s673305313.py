a,b = map(str, input().split())
if int((int(a+b))**(1/2)) == (int(a+b))**(1/2):
    print('Yes')
else:
    print('No')