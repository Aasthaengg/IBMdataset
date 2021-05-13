# coding: utf-8
# Here your code !

while 1 :
    try:
        h,w=map(int,input().split())
        #print(h,w)
        if( h==0 and w==0 ): 
            break
        else:
            for hi in range(h):
                out=""
                if (hi==0 or hi==h-1):
                    out+="#"*w
                else :
                    for wi in range(w):
                        if(wi==0 or wi==w-1): out+="#"
                        else: out+="."
                print(out)
            print()
        if( h==0 and w==0 ): break
    except (EOFError):
        #print("EOFError")
        break