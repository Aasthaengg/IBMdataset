n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
print('#'*(m+2))
for i in range(n):
    print('#'+l[i]+'#')
print('#'*(m+2))
