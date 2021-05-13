import sys
def valid():
    s = input()
    if s=='Vacant':
        sys.exit()
    return 1 if s=='Male' else 0

n = int(input())
print(0, flush=True)
s_l = valid()
lidx = 0
ridx = n

while True:
    midx = (lidx+ridx)//2
    print(midx, flush=True)
    s_m = valid()
    if ((midx-lidx)%2==1) ^ (s_l==s_m):
        lidx = midx
        s_l = s_m
    else:
        ridx = midx