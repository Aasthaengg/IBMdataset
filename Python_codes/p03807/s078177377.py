def main():
    N = int(input())
    A = list(map(int,input().split()))

    bucket = [0]*2

    for i in range(N):
        if A[i]%2 == 0:
            bucket[0] += 1
        else:
            bucket[1] += 1

    if bucket[1]%2 == 0:
        return 'YES'
    else:
        return 'NO'

print(main())
