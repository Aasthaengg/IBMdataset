s = input()

list = ["","Sunny","Cloudy","Rainy"]

result = list.index(s)%3

print(list[result+1])