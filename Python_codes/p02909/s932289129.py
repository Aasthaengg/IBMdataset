S = input()
ls = ['Sunny', 'Cloudy', 'Rainy']
index = (ls.index(S) + 1) % 3
print(ls[index])