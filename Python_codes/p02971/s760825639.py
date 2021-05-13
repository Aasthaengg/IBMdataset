import collections
import copy

def solve():
    a = copy.copy(A)
#    print(a)
    a.sort(reverse=True)
#    print(a)
#    print(A)
    if a[0] == a[1]:
        for i in range(N):
            print(a[0])
    else:
        for i in range(N):
            if A[i] == a[0]:
                print(a[1])
            else:
                print(a[0])
    

if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]
    solve()
