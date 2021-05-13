N = int(input())
A, B = list(map(int, input().split()))
P = list(map(int, input().split()))
counter = [0] * 3
for p in P:
    if p <= A:
        counter[0] += 1
    elif p <= B:
        counter[1] += 1
    else:
        counter[2] += 1
print(min(counter))