def main():
    W, a, b = map(int, input().split())

    if (a + a + W)//2 < b:
        if b > a + W:
            print(b - (a + W))
        else:
            print(0)
    elif(a + a + W)//2 > (b + W):
        if a > (b + W):
            print(a - (b + W))
        else:
            print(0)
    else:
        print(0)
main()