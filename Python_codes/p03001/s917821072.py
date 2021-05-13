w,h,x,y=map(int, input().split())
if x*2==w and y*2==h: div=1
else: div=0
print(w*h/2, div)