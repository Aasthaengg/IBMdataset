import itertools

def check(lst, n, x):
    for i in range(2, n+1):
        B = list(itertools.combinations(lst,i))
        for C in B:
            if x == sum(C):
                return True
    return False

n = int(input())
A = [int(i) for i in input().split()]
q = int(input())
m = [int(i) for i in input().split()]

for x in m:
    if x > sum(A):
        print("no")
    elif (x in A) or check(A, n, x):
        print("yes")
    else:
        print("no")

