# ε₯ε
A, B, C = map(int, input().split())

# εΊε
if -100 <= A and B and C <= 100:
    if C >= A and C <= B:
        print('Yes')
    else:
        print('No')