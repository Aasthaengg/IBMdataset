W = ['Sunny', 'Cloudy', 'Rainy', 'Sunny']

S = input()

for i in range(3):
    if W[i] == S:
        print(W[i+1])
        break