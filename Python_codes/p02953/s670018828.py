N,*H=map(int,open(0).read().split())
H[0]-=1
def main():
    for i in range(1,N):
        if H[i-1]<H[i]:
            H[i]-=1
        elif H[i-1]==H[i]:
            continue
        else:
            return 'No'
    return 'Yes'
print(main())