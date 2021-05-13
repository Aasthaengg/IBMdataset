def main():
    s = input()
    weather = ("Sunny", "Cloudy", "Rainy")
    index = (weather.index(s) + 1) % 3
    print(weather[index])

main()