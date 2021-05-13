def main():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())

    print("YES" if abs(a-b) <= (v-w)*t else "NO")


if __name__ == '__main__':
    main()
