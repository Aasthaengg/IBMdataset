N = int(input())
B = 0
for a in list(map(int, input().split())):
    B += 1/a
print(1/B)