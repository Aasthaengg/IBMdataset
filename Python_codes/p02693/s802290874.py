K = int(input())
A, B = [int(_) for _ in input().split()]

a = B // K

if a*K >= A:
    print("OK")
else:
    print("NG")