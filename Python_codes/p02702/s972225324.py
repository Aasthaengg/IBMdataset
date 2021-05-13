import sys
def main():
    s=sys.stdin.readline().strip()
    x=[0 for _ in [0]*2020]
    x[0],c=1,0
    m,d=0,1
    for i in reversed(s):
        m+=(int(i)*d)
        x[m%2019]+=1
        d=(d*10)%2019
    for v in x:c+=v*(v-1)//2
    print(c)
if __name__=='__main__':main()