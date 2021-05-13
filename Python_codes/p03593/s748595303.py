import sys,math,collections,itertools,heapq
input = sys.stdin.readline

def m(n):
    return -1*n

a = []
H,W=list(map(int,input().split()))
for _ in range(H):
    s = input().rstrip()
    a += list(s)
ac = collections.Counter(a)
acval = sorted(ac.values())

#両方偶数
if H%2 == 0 and W%2==0:
    flag = [4]*((H*W)//4)

#どっちか奇数
elif H%2 ==1 and W %2 == 0:
    flag = [2]*(W//2)+[4]*((H*W-W)//4)
elif W%2 ==1 and H %2 == 0:
    flag = [2]*(H//2)+[4]*((H*W-H)//4)

#両方奇数
if H%2 == 1 and W%2==1:
    flag = [1]+[2]*(H//2)+[2]*(W//2)+[4]*((H*W-1-(W-1)-(H-1))//4)
flag.sort()
acval = list(map(m,acval))
heapq.heapify(acval)
while acval:
    tmpq = -1*heapq.heappop(acval)
    tmpf = flag.pop()
    if tmpq < tmpf:
        print('No')
        exit()
    else:
        tmp = tmpq - tmpf
        if tmp !=0:
            heapq.heappush(acval,-1*tmp)
print('Yes')
