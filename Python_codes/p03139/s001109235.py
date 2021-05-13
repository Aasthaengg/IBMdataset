def main():
    N, A, B = map(int, input().split())
    
    if A + B >= N:
        mini = (A + B) - N
    else:
        mini = 0

    maxi = min(A, B)

    print(maxi, mini)

if __name__ == "__main__":
    main()