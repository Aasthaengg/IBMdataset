import sys
def main():
    s=sys.stdin.readline().strip()
    d,m,p,c={0:1},0,1,0
    for a in reversed(s):
        m+=(int(a)*p)
        k=m%2019
        p=(p*10)%2019
        d[k]=d[k]+1 if k in d else 1
    for v in d.values():c+=v*(v-1)//2
    print(c)
if __name__=='__main__':main()