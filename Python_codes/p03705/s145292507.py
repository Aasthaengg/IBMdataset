n,a,b = map(int, input().split())
if a > b or (n==1 and a != b):
    print(0)
else:
    Max = a + b * (n-1)
    Min = a * (n-1) + b
    print(Max - Min + 1)