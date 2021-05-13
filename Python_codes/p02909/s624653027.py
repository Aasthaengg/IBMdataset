def main():
    S = input()
    weather = ['Sunny', 'Cloudy', 'Rainy']
    idx = 0
    for i,s in enumerate(weather):
        if s == S:
            idx = i+1
    print(weather[idx]) if idx != 3 else print(weather[0])

if __name__ == '__main__':
    main()
