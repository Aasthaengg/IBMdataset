def main():
    a,b = tuple([int(t)for t in input().split()])

    if a<6:
        print(0)
    elif a<13:
        print(b//2)
    else:
        print(b)
if __name__ == "__main__":
    main()