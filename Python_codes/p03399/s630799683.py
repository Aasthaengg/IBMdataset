A,B,C,D = [int(input()) for _ in range(4)]
count = 0
if A < B:
    count += A
else:
    count += B
if C < D:
    count += C
else:
    count += D

print(count)
