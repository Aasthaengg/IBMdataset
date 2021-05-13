k, t = map(int, input().split())
A = list(map(int, input().split()))
if max(A) < k//2+1:
    print(0)
else:
    print(max(A)-(sum(A)-max(A))-1)