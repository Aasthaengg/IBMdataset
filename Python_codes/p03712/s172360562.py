h,w=map(int,input().split())
list1=[[0 for i in range(w)]for j in range(h)]
for i in range(h):
    list1[i]=list(map(str,input().split()))
print('#'*(w+2))
for i in range(h):
    print('#'+str(''.join(list1[i]))+'#')
print('#'*(w+2))