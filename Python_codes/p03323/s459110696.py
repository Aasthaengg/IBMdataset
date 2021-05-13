def main():
    a,b = list(map(int, input().split()))
    print("Yay!" if a < 9 and b < 9 else ":(")

if __name__ == '__main__':
    main()