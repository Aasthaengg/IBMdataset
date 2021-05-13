s = input()
tenki = ["Sunny", "Cloudy", "Rainy" ]
print(tenki[tenki.index(s)+1] if s != "Rainy" else tenki[0])