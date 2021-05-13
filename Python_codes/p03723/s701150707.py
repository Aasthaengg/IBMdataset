import sys
import copy
a = [int(c) for c in input().split()]
cnt=0
while True:
    if a[0]==a[1] and a[1]==a[2] and a[0] != 1:
        print(-1)
        sys.exit(0)
    
    if a[0]%2 == 0 and a[1]%2 == 0 and a[2]%2 == 0:
        b = copy.deepcopy(a)
        a[0] = int((b[1]+b[2])/2)
        a[1] = int((b[2]+b[0])/2)
        a[2] = int((b[0]+b[1])/2)
    else:
        print(cnt)
        sys.exit(0)

    cnt+=1