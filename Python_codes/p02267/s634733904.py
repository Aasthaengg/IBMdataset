n = int(input())
S = set(map(int, input().split()))
q = int(input())
T = set(map(int, input().split()))

count = 0
for x in T:
    count += 1 if x in S else 0

print(count)