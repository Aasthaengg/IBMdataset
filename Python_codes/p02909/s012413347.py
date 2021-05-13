import sys
input = sys.stdin.readline

weather = {"Sunny":"Cloudy", "Cloudy":"Rainy", "Rainy":"Sunny"}

print(weather[input().rstrip()])
