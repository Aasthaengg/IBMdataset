class gv:
    input = None;
    
def build():
    gv.str = input()

def solve():
    slen = len(gv.str)
    if (slen&1) == 1:
        print("No")
        return
    
    for i in range(0,slen,2):
        if (gv.str[i:i+2] == "hi") :
            pass
        else :
            print("No")
            return
    
    print("Yes")
    
    

build()
solve()
