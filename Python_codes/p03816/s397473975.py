N = int(input())
A = set(list(map(int, input().split())))
if len(A)%2:
    print(len(A))
else:
    print(len(A)-1)