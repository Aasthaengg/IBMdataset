
def main():
    x, y = map(int,input().split())

    if x % y == 0:
        print(-1)
        exit()


    i=0
    while True:
        if x * i % y == 0:
            i+=1
        else:
            print(x)
            exit()


if __name__ == "__main__":
        main()
