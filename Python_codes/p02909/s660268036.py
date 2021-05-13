Weather = ['Sunny','Cloudy','Rainy']
S = input()
for i,s in enumerate(Weather):
    if s == S:
        print(Weather[(i+1)%3])
