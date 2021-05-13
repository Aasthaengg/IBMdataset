if __name__ == "__main__":
    n = int(input())
    F = [1, 1]
    for i in range(n-1):
        F.append(F[-2]+F[-1])
    print(F[n])