INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    s=STR()
    cnt=[0]*2019
    cnt[0]=1
    temp=0
    keta=1
    ans=0
    for i in s[::-1]:
        temp=(temp+int(i)*keta)%2019
        keta=(keta*10)%2019
        cnt[temp]+=1
    for i in cnt:
        ans+=(i*(i-1))//2
    print(ans)
    
    
if __name__ == '__main__':
    do()