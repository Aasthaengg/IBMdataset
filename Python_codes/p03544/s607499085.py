# ABC079 B - Lucas Number

n = int(input())
a=[2,1]
a_tes = 0

for i in range(2,n+1):
    a_tes = a[i-1] + a[i-2]
    a.append(a_tes)
print(a[n])