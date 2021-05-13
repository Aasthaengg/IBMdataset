K = int(input())
A, B = map(int, input().split())
large = (B // K) * K
if A <= large:
    print("OK")
else:
    print("NG")
