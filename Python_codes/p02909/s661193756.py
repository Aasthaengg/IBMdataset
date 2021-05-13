S = str(input())
l= ['Sunny','Cloudy','Rainy']

for i in range(2):
    if S == l[2]:
        print('Sunny')
        exit()
    elif S == l[i]:
        print(l[i+1])
        exit()