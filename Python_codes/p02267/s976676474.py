n = int(raw_input())
S = map(int, raw_input().split())
q = int(raw_input())
T = map(int, raw_input().split())
count = 0
for x in T:
    if x in S:
        count += 1
print count