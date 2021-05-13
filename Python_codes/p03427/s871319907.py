def main():
    a = 0
    b = False
    for i,v in enumerate(input()):
        if i == 0:
            a += int(v)
        else:
            b = int(v) < 9
            a += 9
    print(a-b)

if __name__ == "__main__":
    main()