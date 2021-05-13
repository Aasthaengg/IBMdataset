#a=int(input())
#b,c=int(input()),int(input())
# c=[]
#  for i in b:
#     c.append(i)
N,X = map(int,input().split())
# f = list(map(int,input().split()))
#j = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
a=[]
for i in range(N):
    m=int(input())
    a.append(m)
b=min(a)
c=(X-sum(a))//b
print(c+N)
