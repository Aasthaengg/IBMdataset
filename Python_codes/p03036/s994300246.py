def main():
    r, D, x = map(int, input().split())
    for i in range(1, 11):
        x = r*x - D
        print(int(x))
main()