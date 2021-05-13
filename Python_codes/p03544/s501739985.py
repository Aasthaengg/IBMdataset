def main():
    L = [2, 1]
    for _ in range(86):
        L.append(L[-1] + L[-2])
    
    N = int(input())
    print(L[N])

if __name__ == "__main__":
    main()
