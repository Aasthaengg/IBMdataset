N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

s1, s2, s3 = 0, 0, 0
for p in P:
    if p <= A:
        s1 += 1
    elif A+1 <= p <= B:
        s2 += 1
    else:
        s3 += 1
print(min(s1, s2, s3))