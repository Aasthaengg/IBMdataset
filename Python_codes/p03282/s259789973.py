import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    k=int(input())
    if s[0]!='1':
        print(s[0])
    else:
        cnt=0
        tugi=''
        for i in s:
            if i=='1':
                cnt+=1
            else:
                tugi=i
                break
        if cnt>=k:
            print('1')
        else:
            print(tugi)
resolve()