w,h,x,y=map(int,input().split())
p=1 if w==x*2 and h==y*2 else 0
print("{:.10f}".format((w*h)/2),p)