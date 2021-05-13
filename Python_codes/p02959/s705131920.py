def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split())) 
    e = sum(B)
    for i in range(len(B)):
        attack = min(B[i],A[i])
        B[i] -= attack
        A[i] -= attack

        if i < N:
            attack = min(B[i],A[i+1])
            B[i] -= attack
            A[i+1] -= attack

    print(e-sum(B))



if __name__ == '__main__':
    main()
