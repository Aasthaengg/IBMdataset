def main():
    N, A, B = list(map(int, input().split()))

    delta = abs(A-B) -1

    if delta%2:
        print("Alice")
    else:
        print("Borys")

main()