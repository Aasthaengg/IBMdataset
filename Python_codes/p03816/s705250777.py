input()
A = list(map(int, input().split()))
a = len(set(A))
res = len(A)-a
print(a-1) if res%2 else print(a)