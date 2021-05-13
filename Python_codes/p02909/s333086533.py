S = input()
T = ["Sunny", "Cloudy", "Rainy", "Sunny"]

for i in range(len(T)):
    if S == T[i]:
        print(T[i+1])
        break