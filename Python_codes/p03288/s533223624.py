def main():
    R = int(input())
    if R < 1200:
        return "ABC"
    elif R < 2800:
        return "ARC"
    else:
        return "AGC"

if __name__ == '__main__':
    print(main())
