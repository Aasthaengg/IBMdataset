import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    
    dp = [False for _ in range(M+1)]

    for i in range(M+1):
        for num in a:
            if i-num<0:
                continue
            if dp[i-num] == False:
                dp[i] = True

    if dp[M]:
        print("First")
    else:
        print("Second")
   
if __name__ == "__main__":
    main()
