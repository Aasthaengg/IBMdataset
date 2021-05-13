N = map(int, input().split())
A = list(map(int, input().split()))
reverse = 0

for a in A:
    reverse += 1 / a

print(reverse**-1)