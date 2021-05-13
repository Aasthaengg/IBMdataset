import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    num=0
    for i in s:
        #'C'がまだ見つかっていない状態：num=0
        #'C'が見つかって'F'がまだ見つかっていない状態:num=1
        #'C'が見つかってから'F'が見つかった状態:num=2
        #num==0のときに'C'が見つかったらnumを１にする
        #num==１のときに'F'が見つかったらnumを２にする
        if i=='C' and num==0:
            num+=1
        if i=='F' and num==1:
            num+=1
    if num==2:
        print('Yes')
    else:
        print('No')
resolve()