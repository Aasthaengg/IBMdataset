N=int(input())
t_pre=0
x_pre=0
y_pre=0

for i in range(N):
    t,x,y = map(int,input().split())
    t_af=t-t_pre
    x_af=x-x_pre
    y_af=y-y_pre
    if (abs(x_af+y_af)<=t_af) & ((x_af+y_af+t_af)%2 == 0):
      t_pre=t
      x_pre=x
      y_pre=y
      continue
    else:
        print("No")
        exit()
print("Yes")
