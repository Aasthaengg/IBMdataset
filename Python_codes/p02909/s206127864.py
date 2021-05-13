S = input()
L = ["Sunny", "Cloudy", "Rainy"]

for i in range(3):
  if L[i] == S:
    print(L[(i+1)%3])