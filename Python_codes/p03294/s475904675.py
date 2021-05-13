N = int(input())
A = list(map(lambda a:int(a), input().split(" ")))
print(sum(A) - len(A))