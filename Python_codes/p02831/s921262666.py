A, B = list(map(int, input().split()))

large = A if A > B else B
small = A if A < B else B

def gcd(large, small):
    r = large % small
    while r != 0:
        large = small
        small = r
        r = large % small
    return small

print(large*small//gcd(large, small))
