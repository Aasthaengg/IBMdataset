A, B, C = map(int, input().split())
lst=[A,B,C]
for val in lst:
    if lst.count(val)==1:
        print(val)