
def main():
    n = int(input())
    x = list(map(int, input().split(" ")))
    min = 1e9
    for i in range(1,101):
        na = 0
        for j in x:
            na += (j - i)**2
        if na < min:
            min = na
    print(min)
        



if __name__ == "__main__":
    main()