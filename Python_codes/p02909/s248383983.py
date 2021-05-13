l = ["Sunny", "Cloudy", "Rainy"]
s = input()
idx = l.index(s)
print(l[(idx+1)%3])