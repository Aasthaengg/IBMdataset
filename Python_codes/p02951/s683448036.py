def main():
    a, b, c = map(int, input().split())
    bc = b+c
    if a <= bc:
        print(bc-a)
    else:
        print(0)

main()