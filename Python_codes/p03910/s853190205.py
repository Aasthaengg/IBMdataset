import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    if N==1:
        print(1)
        exit()
    temp=0
    ans=[]
    for i in range(1,N+5):
        temp+=i
        ans.append(i)
        if temp>N:
            ans.remove(temp-N)
            break
        elif temp==N:
            break
    for i in range(len(ans)):
        print(ans[i])
        

main()
