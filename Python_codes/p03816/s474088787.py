#053_D
n = int(input())
a = list(map(int, input().split()))
sa = set(a)
x = n - len(sa)
print(len(sa) if x % 2 == 0 else len(sa) - 1)