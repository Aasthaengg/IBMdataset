A, B = map(int, input().split())

A_x = (B-A)-1

print(sum(list(range(A_x+1)))-A)
