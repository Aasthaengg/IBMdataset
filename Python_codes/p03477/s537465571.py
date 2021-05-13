def main():
    A, B, C, D = map(int, input().split())
    left = A + B
    right = C + D
    ans = "Left" if left > right else "Balanced" if left == right else "Right"
    print(ans)


if __name__ == "__main__":
    main()
