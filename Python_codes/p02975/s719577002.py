from collections import Counter
def solve():
    N=int(input())
    A=list(map(int,input().split()))

    cnt=Counter(A)

    if cnt[0]==N:
        print("Yes")
        return
    t=0
    for a in A:
        t^=a

    if N%3==0:
        if cnt[0]==int(N//3) and len(cnt)==2:
            print("Yes")
        elif len(cnt)==3 and t==0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


    
if __name__ == "__main__":
     solve()
