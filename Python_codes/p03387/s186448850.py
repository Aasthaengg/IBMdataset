lis = list(map(int, input().split()))

a,b,c = sorted(lis)

bc = c-b
ab = b-a

if ab % 2 == 0:
    print(bc + ab//2)
else:
    print(bc+(ab//2) +2)