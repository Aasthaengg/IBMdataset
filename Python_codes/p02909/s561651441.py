n=input()
l=[ "Sunny","Cloudy", "Rainy","Sunny"]
for i in range(3):
    if n==l[i]:
        print(l[i+1])
        break