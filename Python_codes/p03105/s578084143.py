A,B,C = list(map(int,input().split()))
count = B // A
if count < C:
    print(count)
else:
    print(C)