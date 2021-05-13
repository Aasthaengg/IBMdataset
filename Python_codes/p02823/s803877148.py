def main():
    N, A, B = map(int, input().split())

    if abs(A-B) % 2 == 0:
        print(abs(A-B)//2)
    else:
        print(min([A-1, N-B])+1+(B-A-1)//2)


if __name__ == "__main__":
    main()
