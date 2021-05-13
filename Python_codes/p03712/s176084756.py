h,w=map(int,input().split())
a=[]
for i in range(h):
    a.append(input())
print("#"*(w+2))
for i in range(len(a)):
    print("#"+a[i]+"#")
print("#"*(w+2))