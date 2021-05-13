a = list(map(int, input().split()))
if a[0]==1 and a[1]==1:
    print(1)
    exit()
if a[0]==1 or a[1]==1:
    print(max(max(a)-2, 0))
    exit()
print((a[0]-2)*(a[1]-2))
