def main():
    n=input()
    a=map(int,input().split())
    c = 0
    for x in (i for i in a if i % 2 == 0):
        while True:
            if x % 2 == 0:
                x //= 2
                c += 1
            else:
                break
    print(c)
    
if __name__ == "__main__":
    main()