#a=int(input())
#b,c=int(input()),int(input())
# c=[]
#  for i in b:
#     c.append(i)
#e1,e2 = map(int,input().split())
f = list(map(int,input().split()))
K=int(input())
#j = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
f.sort(reverse=True)
for i in range(K):
    f[0]*=2
print(sum(f))