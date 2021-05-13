import sys
input = sys.stdin.readline

def bubble_sort(A):
    flag = 1  # if non-sorted element exist on side
    counter = 0
    while flag:
        flag = 0
        for i in range(1, len(A))[::-1]:
            if A[i] < A[i - 1]:
                counter += 1
                A[i], A[i - 1] = A[i - 1], A[i]
                flag = 1
    return (A,counter)


def main():
    _,k = [int(i) for i in input().strip().split()]
    l = [int(i) for i in input().strip().split()]
    _sorted, inner = bubble_sort(l)
    _, outer = bubble_sort(_sorted + _sorted)
    
    print((inner * k + (k * (k - 1) // 2) * outer) % (10 ** 9 + 7))
    
if __name__ == "__main__":
    main()