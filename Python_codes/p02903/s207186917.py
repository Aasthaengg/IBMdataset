h,w,a,b=map(int,input().split())
if a>w//2or b>h//2:print('No')
else:
 for i in range(h):t=i<b;print(('0'*(w-a)+'1'*a)*(1-t)+('1'*(w-a)+'0'*a)*t)