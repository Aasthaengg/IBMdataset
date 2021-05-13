_ = input()
A = [int(i) for i in input().split()]
result = {True: "APPROVED", False: "DENIED"}
print(result[all([a % 2 == 1 or (a % 3 == 0 or a % 5 == 0) for a in A])])