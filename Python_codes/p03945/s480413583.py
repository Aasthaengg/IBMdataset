import sys
def v():
    S=sys.stdin.readline().strip()
    c,res=S[0],0
    for s in S:
        if c!=s:c,res=s,res+1
    print(res)
if __name__=='__main__':v()