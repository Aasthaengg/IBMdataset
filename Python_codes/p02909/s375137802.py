
def main():
    s = input()
    tenki = ['Sunny', 'Cloudy', 'Rainy']
    index = tenki.index(s)
    print(tenki[(index+1) % 3])


if __name__ == "__main__":
    main()
