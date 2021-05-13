A, B = map(int, input().split())
lst = [A+B, A-B, A*B]
lst.sort()
print(lst[-1])