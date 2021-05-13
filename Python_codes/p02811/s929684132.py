def main():
    n, x = map(int, input().split(" "))
    print("Yes" if n*500 >= x else "No")

main()