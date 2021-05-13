def main():
    s = str(input())
    l = ['Sunny', 'Cloudy', 'Rainy']
    if s == 'Rainy':
        print(l[0])
    else:
        print(l[l.index(s) + 1])
main()