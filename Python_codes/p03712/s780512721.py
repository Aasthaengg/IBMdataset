h,w=map(int,input().split())
lst=[input() for i in range(h)]

print("#"*(w+2))
for i in range(h):
    print("#",end="")
    print(lst[i],end="")
    print("#")
print("#"*(w+2))