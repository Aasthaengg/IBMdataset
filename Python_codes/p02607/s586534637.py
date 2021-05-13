import sys
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

if __name__=='__main__':
    n = I()
    a = list(IL())
    c = 0
    for i,item in enumerate(a):
        if (i+1)%2==1 and item%2==1:
            c+=1
    print(c)
    exit()