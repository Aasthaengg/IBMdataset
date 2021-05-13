n,a,b = map(int, input().split( ))
h = [int(input()) for _ in range(n)]
mx = 10**10
mn = 0
#2分探索
while mx-mn>1:
    md = (mx+mn)//2
    h2 = [h[i]-md*b for i in range(n)]
    
    tmp = 0
    for i in range(n):
        if h2[i]>0:
            tmp += (h2[i]+(a-b)-1)//(a-b)
    if tmp<=md:
        mx = md
    else:
        mn = md

print(mx)            

