inp1,inp2=map(int,input().split())
list=[]
for inp2 in range(inp2-inp1+1,inp2+inp1):
               list.append(inp2)
print(*list)