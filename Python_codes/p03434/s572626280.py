def main():
    N = int(input())
    a = list(map(int,input().split()))
    Alice = 0
    Alice_j = True
    Bob = 0
    Bob_j = False
    a.sort(reverse = True )
    for i in range(N):
        if Alice_j == True:
            Alice += a[i]
            Alice_j = False
            Bob_j = True
        elif Bob_j == True:
            Bob += a[i]
            Bob_j = False
            Alice_j = True
    return Alice - Bob

print(main())
