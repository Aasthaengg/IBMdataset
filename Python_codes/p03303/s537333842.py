

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    w=I()
    ans=[]
    for i in range(0,len(S),w):
        ans.append(S[i])
        
    print(''.join(map(str,ans)))

main()
