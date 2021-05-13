wet = ["Sunny","Cloudy","Rainy"]
s = wet.index(input())
print(wet[s+1] if s != 2 else wet[0])
