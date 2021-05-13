h,w=map(int,input().split())
li=[]
for _ in range(h):
    a=input()
    li.append(a)
print('#'*(w+2))
for i in li:
    print('#'+i+'#')
print('#'*(w+2))