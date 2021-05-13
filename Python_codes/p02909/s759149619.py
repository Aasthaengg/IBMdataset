s=input()

wether=['Sunny', 'Cloudy', 'Rainy']

num=(wether.index(s)+1)%3

print(wether[num])