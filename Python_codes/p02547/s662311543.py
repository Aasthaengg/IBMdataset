N,*D=map(int,open(0).read().split())
def main():
    cnt=0
    for i in range(0,N*2,2):
        n1=D[i]
        n2=D[i+1]
        if n1==n2:
            cnt+=1
            if cnt>=3:
                return True
        else:
            cnt=0
    return False
if main():
    print("Yes")
else:
    print("No")