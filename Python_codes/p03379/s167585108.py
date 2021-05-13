n=int(input())
lst=list(map(int,input().split()))
sorted_lst=sorted(lst)

a=n//2
p=sorted_lst[a-1]
q=sorted_lst[a]

for i in range(n):
    if lst[i]<=p:
        print(q)
    else:
        print(p)