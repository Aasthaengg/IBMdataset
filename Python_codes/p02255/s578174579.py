import sys
def print_list(A):
    for k in range(len(A)):
        sys.stdout.write(str(A[k]))
        if not k == len(A) -1: sys.stdout.write(" ")
    print()
def insert_sort(A,N):
    print_list(A)
    for i in range(1,N):
        v = A[i]
        j = i-1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j = j-1
        A[j+1]=v
        print_list(A)


N = int(input())
A = list(map(int,input().split()))
insert_sort(A,N)