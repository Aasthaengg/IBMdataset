n, m = map(int, input().split())

if n % 2 == 1:
    for i in range(m):  
        print(i+1, n-i)
else:
    middle = int((m+1)/2)
    for i in range(middle):
        print(i+1, n-i)
    for i in range(middle, m):
        print(i+2, n-i)