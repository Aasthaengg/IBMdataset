n,m = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)
v = sum(a)

# for i in range(1,m+1):
#     if a[i-1] < v/(4*i):
#         print("No")
#         exit(0)

if a[m-1] < v/(4*m):
    print("No")
else:
    print("Yes")
