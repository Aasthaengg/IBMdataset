c = input().split()
n = list(map(int, input().split()))
if input() == c[0]:
    n[0] -= 1
else:
    n[1] -= 1
print(n[0], n[1])