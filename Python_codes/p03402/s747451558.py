h,w=100,100
a,b=map(int,input().split())
u=[['#']*w for i in range(h//2)]
d=[['.']*w for i in range(h//2)]


for i in range(a-1):
    u[1+((2*i)//w)*2][(2*i)%w]='.'

for i in range(b-1):
    d[1+((2*i)//w)*2][(2*i)%w]='#'
    
g=u+d
    
print(h,w)
for j in g:
    print(''.join(j))

