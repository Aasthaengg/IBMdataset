x = ["Sunny", "Cloudy", "Rainy"]
y = input()
if y == "Rainy":
    print(x[0])
else:
    print(x[x.index(y)+1])
