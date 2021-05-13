w = ['Sunny', 'Cloudy','Rainy']
S = input()
i = w.index(S)
print(w[(i+1) % 3])