def main():
    A, B = map(int, input().split())
    d = max(A, B) - min(A, B)
    if d % 2 == 0:
        K = min(A, B) + d//2
        print(K)
    else:
        print("IMPOSSIBLE")
if __name__ == "__main__":
    main()