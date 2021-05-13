
def main():
    s = input()
    if s[1] == "S":
        if s[0] == "R" or s[2] == "R":
            print(1)
        else:
            print(0)
    else:
        count = 0
        for i in range(3):
            if s[i] == "R":
                count += 1
        print(count)

if __name__ == '__main__':
    main()
