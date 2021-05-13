def chess(h,w):
    o = ""
    for i in range(h):
        for j in range(w):
            if (i+j)%2: o+="." 
            else: o+="#"
        o+="\n"
    print o

while 1:
    h,w=map(int,raw_input().split())
    if h==w==0:break
    chess(h,w)