lst=input().split()
lst=list(map(lambda i:float(i),lst))
x_1=lst[0]
x_2=lst[1]
y_1=lst[2]
y_2=lst[3]
dis=((x_1-y_1)**2+(x_2-y_2)**2)**(1/2)
print(dis)


