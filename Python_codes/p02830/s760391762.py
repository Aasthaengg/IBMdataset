def main():
    n = int(input())
    s, t = input().split(" ")
    print("".join(a+b for a, b in zip(s, t)))


main()