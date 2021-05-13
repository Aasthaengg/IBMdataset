def main():
    x, a, b = map(int, input().split())

    if b <= a:
        print("delicious")
    elif a < b and b <= a + x:
        print("safe")
    elif a + x < b:
        print("dangerous")
main()