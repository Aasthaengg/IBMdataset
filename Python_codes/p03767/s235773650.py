N=int(input())
a=input().split()
a=[int(x) for x in a]
a.sort(reverse=True)
s=0
for i in range(N):
    s+=a[2*i+1]

print(s)