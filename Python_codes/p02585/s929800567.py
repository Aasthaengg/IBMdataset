import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from itertools import accumulate

def circle_sum_max(circle,num):
    n = len(circle)
    s = sum(circle)
    if num == 0:
        ans = 0
    elif num == 1:
        ans = max(circle)
    else:
        ac = list(accumulate([0]+circle))

        l = 0
        r = 1
        ans = ac[r]-ac[l]
        i = 0
        while r!=n or i%2==1:
            if i%2==0:
                r = ac[r+1:l+num+1].index(max(ac[r+1:l+num+1])) + r+1
            else:
                l = ac[l+1:r].index(min(ac[l+1:r])) + l+1
            i+=1
            ans = max(ans,ac[r]-ac[l])
 
        num = n-num
        l = 0
        r = num
        i = 0
        ans = max(ans,s-ac[r]+ac[l])
        while r!=n or i%2==1:
            if i%2==0:
                r = ac[r+1:l+n].index(min(ac[r+1:l+n])) + r+1
            else:
                l = ac[l+1:r-num+1].index(max(ac[l+1:r-num+1])) + l+1
            i+=1
            ans = max(ans,s-ac[r]+ac[l])
    return ans
 

n,k = readints()
p = [x-1 for x in readints()]
c = readints()

circles = []
used = [0]*n

for i in range(n):
    if not used[i]:
        circles.append([c[i]])
        used[i] = 1
        j = p[i]
        while not used[j]:
            circles[-1].append(c[j])
            used[j] = 1
            j = p[j]

score = -10**20

for cir in circles:
    m = len(cir)
    a = sum(cir)
    if k>m:
        if a>0:
            score = max(score, (k//m)*a + circle_sum_max(cir,k%m), (k//m-1)*a + circle_sum_max(cir,m))
        else:
            score = max(score,circle_sum_max(cir,m))
    else:
        score = max(score,circle_sum_max(cir,k))

print(score)








