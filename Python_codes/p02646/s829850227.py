def main():
    A, V = (int(i) for i in input().split())
    B, W = (int(i) for i in input().split())
    T = int(input())
    if A == B:
        print("YES")
    elif V <= W:
        print("NO")
    elif abs(A-B) <= (V-W)*T:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
