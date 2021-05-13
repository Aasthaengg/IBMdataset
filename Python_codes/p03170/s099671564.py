def stones(a,k): # k個の石を取り合う a[i](sorted)個とることが可能な時必勝はどちらか
    n=len(a)
    dp=[False for _ in range(k+1)] #石がi個の時、dp[i]=Trueで勝利Falseで敗北
    for i in range(k+1):
        for j in range(n):
            if i-a[j]>=0:
                if not dp[i-a[j]]:
                    dp[i]=True
    if dp[k]:
        print("First")
    else:
        print("Second")


def main():
    n,k = map(int,input().split()) 
    a = list(map(int,input().split()))
    a.sort()
    stones(a,k)
if __name__ == "__main__":
    main()
