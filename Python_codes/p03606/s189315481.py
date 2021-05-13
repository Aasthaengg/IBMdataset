icase=0
if icase==0:
    n=int(input())
    ncnt=0
    for i in range(n):
        li,ri=map(int,input().split())
        ncnt=ncnt+ri-li+1
    print(ncnt)