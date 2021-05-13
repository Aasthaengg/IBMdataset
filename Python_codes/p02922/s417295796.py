import sys
d = list(map(int,input().split()))
A = d[0]
B = d[1]
cnt = 0
while True:
    #A口がcnt個ある。cntが1のときA*1口
    #cntが2以上のとき、
    if A*cnt - cnt +1 >= B:
        print(cnt)
        sys.exit(0)
    cnt +=1
