if __name__=="__main__":
    n, A, B = input().split(' ')
    n = int(n)
    A = int(A)
    B = int(B)
    print(min(A, B),  max(B - (n - A), 0))