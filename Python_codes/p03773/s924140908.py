
def main():
    a, b = list(map(int, input().split()))
    ans = a + b
    if ans >= 24:
        print((24-ans)*-1)
    else:
        print(ans)



if __name__ == '__main__':
    main()