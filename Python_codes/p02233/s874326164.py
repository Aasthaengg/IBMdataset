if __name__ == "__main__":
    n = input()
    F = []
    F.append(1)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-1] + F[i-2])

    print(F[n])