n = int(input())

l = list(map(int, input().split()))

value = 0

for i in l:
    value = value+1/i

print(1/value)