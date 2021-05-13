def frame(h,w):
    m,b,p = "#","\n","."
    return m*w+b + (m+p*(w-2)+m+b)*(h-2) + m*w+b

while 1:
    h,w=map(int,raw_input().split())
    if h==w==0:break
    print frame(h,w)