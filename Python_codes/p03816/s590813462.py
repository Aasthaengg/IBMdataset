N = int(input())
A = list(map(int,input().split()))
As = set(A)
print(len(As)-(N - len(As))%2)