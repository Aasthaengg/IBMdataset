
def main():
    s = input()
    if len(s) == 2:
        print(s)
    else:
        print(s[::-1])
    pass

if __name__ == '__main__':
    main()