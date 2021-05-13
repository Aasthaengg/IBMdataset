# import math
# import statistics
# import itertools
# a=int(input())
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
A,B= map(int,input().split())
f = list(map(int,input().split()))
# g = [input().split for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

okasi=B
f.sort()
ans=0
for i in range(A):
    if B>=f[i]:
        B=B-f[i]
        ans+=1
    else:
        if B==okasi:
            ans=0
        break
    if B>0 and i==A-1:
        ans-=1

    


print(ans)
