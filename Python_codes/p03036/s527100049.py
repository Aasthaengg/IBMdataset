def main():
    r, D, x2000 = map(int, input().split())
    x = x2000
    for i in range(1, 11):
        print(int(r*x - D))
        x = r*x - D
main()