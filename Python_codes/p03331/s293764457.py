N=int(input())
#A=1B=N-1にしてAとBの各位の和を出す
f_x=sum(map(int,str(N-1)))
count=int((f_x)+1)
for a in range(1,N):
    f_x_a=sum(map(int,str(a)))
    b=N-a
    f_x_b=sum(map(int,str(b)))
    ans=int((f_x_a)+(f_x_b))
#f_xより小さかったらcountに入れていきたい
    if count>=ans:
        count=ans
print(count)