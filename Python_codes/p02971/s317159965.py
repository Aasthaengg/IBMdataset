n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
sort_a=sorted(a,reverse=True)
for i in range(n):
    if a[i]==sort_a[0]:
        print(sort_a[1])
    else:
        print(sort_a[0])