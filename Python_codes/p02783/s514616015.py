def main():
    a, b = map(int, input().split())
    count = 0
    while a > 0:
        count += 1
        a = a - b
    print(count)
main()