step,pay,gain=map(int,input().split())
b=step-pay+1
print(max(step+1,pay+b//2*(gain-pay)+b%2))
