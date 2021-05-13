n=int(input())
a=[int(input())for i in range(n)]
a_max=max(a)
index_max=a.index(a_max)
for i in range(n):
    if i==index_max:
        print(max(a[:index_max]+a[index_max+1:]))
    else:
        print(a_max)