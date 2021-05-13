import math
def main():
    n,h = map(int,input().split())
    A =0
    BA = []
    for i in range(n):
        a,b = map(int,input().split())
        BA.append([b,a])
        A = max(A,a)
    BA.sort(reverse=True)
    cnt = 0
    for i in range(n):
        if BA[i][0]> A:
            h -= BA[i][0]
            cnt += 1
            if h <= 0:
                break
    
    if h>0:
        cnt += math.ceil(h/A)
    print(cnt)

main()
