n=int(input())
a=[0]*n
for i in range(n):
    a[i] = int(input())

a_set=set(a)
print(len(a_set))