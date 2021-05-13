n,k=map(int, input("").split(' '))
assert n>=k>=1
assert 1<=n<=50

s=input('')
assert ("a","b","c" in s)

z=list((s))
z[k-1]=z[k-1].swapcase()

for i in z:
    print(i, end='')



  
 

