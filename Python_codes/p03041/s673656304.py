n,k=map(int,input().split())
a = input()
 
a = list(a)
a[k - 1] = a[k-1].lower()
a = "".join(a)
print(a)