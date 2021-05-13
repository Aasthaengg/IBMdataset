
def main():
    n = int(input())
    a = int(input())
    n = n % 500
    if n <= a:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
