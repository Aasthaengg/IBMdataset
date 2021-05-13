A, B = map(int,input().split())
# N = int(input())
# al = list(map(int,input().split()))

start = A + B
if start > 23:
    print(start - 24)
else:
    print(start)