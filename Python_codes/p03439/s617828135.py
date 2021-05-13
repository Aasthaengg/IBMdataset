import sys
def query(i):
    print(i)
    sys.stdout.flush()
    s=input()
    if s=="Vacant":
        exit()
    return s=="Male"

def main():
    N=int(input())
    al=ar=query(0)
    l,r=0,N
    while True:
        m=(l+r)//2
        am=query(m)
        if al==am and (m-l)%2==1 or al!=am and (m-l)%2==0:
            r,ar=m,am
        else:
            l,al=m,am

if __name__ == "__main__":
    main()