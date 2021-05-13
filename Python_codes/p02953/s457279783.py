N,*H=map(int,open(0).read().split())
H[0]-=1
def main():
    ihmax=0
    hmax=H[0]
    for i in range(1,N):
        if H[i-1]<H[i]:
            ihmax=i-1
            H[i]-=1
            hmax=max(H[i],hmax)
        elif H[i-1]==H[i]:
            continue
        else:
            return 'No'
    return 'Yes'
print(main())