h,w=map(int,input().split())
c=[input() for _ in range(h)]
s=''
for i in range(2*h):
    s+=f'{c[i//2]}\n'
print(s)
