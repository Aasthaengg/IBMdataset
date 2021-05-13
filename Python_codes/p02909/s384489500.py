import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    weather = ['Sunny', 'Cloudy', 'Rainy', 'Sunny']
    print(weather[weather.index(s)+1])

if __name__ == '__main__':
    main()