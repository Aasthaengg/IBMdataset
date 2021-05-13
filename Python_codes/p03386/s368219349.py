a, b, k = map(int, input().split())
for i in range(k):
    if a+i <= b:
        print(a+i)
for i in range(k-1,-1,-1):
    if b-i > a+k-1:
        print(b-i)