
def main():
    s = input().split('/')
    result = int(s[0] + s[1] + s[2])
    if result <= 20190430:
        print('Heisei') 
    else:
        print('TBD')


if __name__ == "__main__":
    main()
