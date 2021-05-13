import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

H, W =LI()
N = I()
a = LI()
c = [[0]*W for i in range(H)]
k = int(0)
cur = int(0)
kin = int(0)
for i,anum in enumerate(a):
#    print(k,cur)
    for j in range(anum):
#        print(k,j)
        if cur%2==0 and (k+j)==W:
            cur +=1
            k = j-1
        if cur%2==1 and (W-j+k)==-1:
            cur +=1
            k = -j
        if cur%2==0:
            c[cur][k+j] = i+1
        else:
            c[cur][W-j+k] = i+1

    if cur % 2 == 0:
        k = k+j+1
    else:
        k = -j+k-1

for v in c:
    print(" ".join(map(str,v)))

