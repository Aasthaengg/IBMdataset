def read_str():
    return input()

def main():
    s = read_str()
    print(s.count('+') * 1 - s.count('-'))

if __name__ == '__main__':
    main()