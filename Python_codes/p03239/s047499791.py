#a=int(input())
#b,c=int(input()),int(input())
# c=[]
#  for i in b:
#     c.append(i)
N,T = map(int,input().split())
# f = list(map(int,input().split()))
#j = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
a=[]
for i in range(N):
    c,d = map(int,input().split())
    if T>=d:
        a.append(c)
if len(a)==0:
    print("TLE")
else:print(min(a))
