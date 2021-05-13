def resolve():
    N = int(input())
    B = list(map(int, input().split()))
    array = [0 for _ in range(N)]
    prev = B[0]
    array[0] = B[0]
    for i in range(N-1):
        if prev <= B[i]:
            array[i+1] = B[i]
        else:
            array[i] = B[i]
            array[i+1] = B[i]
        prev = B[i]
    print(sum(array))

    
if '__main__' == __name__:
    resolve()