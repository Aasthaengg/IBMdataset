H,W=map(int,input().split())
a=[]
for i in range(H):
    a.append(list(input()))
for i in range(len(a)):
    a[i]=['#']+a[i]+['#']
b=[]
for i in range(W+2):
    b.append('#')
print(''.join(b))
for i in range(len(a)):
    print(''.join(a[i]))
print(''.join(b))