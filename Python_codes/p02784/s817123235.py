H, N = list(map(lambda x: int(x), input().split(" ")))
A = list(map(lambda y: int(y), input().split(" ")))
print("Yes") if H <= sum(A) else print("No")