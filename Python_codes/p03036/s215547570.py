def main():
    r, D, x = map(int, input().split())
    for i in range(1, 11):
        print(int(r*x - D))
        x = r*x - D
main()