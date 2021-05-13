# coding = utf-8
n=input("")
a=input("")
a=a.split(" ")
a=[int(s) for s in a]
a.sort()
base=100000
n=1
for num in a:
    while num%2**n==0:
        n=n+1
    n=n-1
    if n < base:
        base=n
print(base)