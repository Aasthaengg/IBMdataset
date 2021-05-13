N = int(input())
A = list(map(lambda a: int(a), input().split(" ")))
print(max(A) - min(A))