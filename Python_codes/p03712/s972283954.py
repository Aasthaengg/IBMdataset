H,W = map(int,input().split())
l=[]
for i in range(H):
    l.append(input())
print('#'*(W+2))
for i in range(H):
    print('#'+l[i]+'#')
print('#'*(W+2))
