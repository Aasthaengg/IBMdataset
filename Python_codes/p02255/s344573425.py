def insert_sort():
    n = int(input())
    A = [int(x) for x in input().split()]
    print(*A)
    for i in range(1,n):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(*A)



if __name__ == "__main__":
    insert_sort()