def main():
    A, B, C = map(int,input().split())
    temp = 1
    for i in range(1, B+1):
        temp = A*i
        if temp%B == C:
            return 'YES'

    return 'NO'

print(main())
