S=input()
climate=['Sunny','Cloudy','Rainy']
i=climate.index(S)
if i==0 or i==1:
    print(climate[i+1])
else:
    print('Sunny')