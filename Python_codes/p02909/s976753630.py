s = input()
li = ['Sunny', 'Cloudy', 'Rainy']
for i in range(3):
    if s==li[i]:
        print(li[(i+1)%3])