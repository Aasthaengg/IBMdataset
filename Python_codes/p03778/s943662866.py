w,a,b=map(int,input().split())
print(0 if b<=a<=b+w or a<=b<=a+w else min(abs(b-a-w),abs(a-b-w)))