N = int(input())
A = list(map(lambda x: int(x), input().split(" ")))
B = list(filter(lambda y: y % 2 == 0 and y % 3 != 0 and y % 5 != 0, A))
print("DENIED") if len(B) > 0 else print("APPROVED")
