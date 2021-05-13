S=input()
weather=['Sunny','Cloudy','Rainy']

for i in weather:
    if i == 'Rainy':
        print('Sunny')
        exit()
    elif i == S:
        a=weather.index(i)
        print(weather[a+1])
        exit()
