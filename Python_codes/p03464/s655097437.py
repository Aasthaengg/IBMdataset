from collections import defaultdict
import sys
input = sys.stdin.buffer.readline

def main():
    K = int(input())
    A = list(map(int,input().split()))
    
    L = [1]
    for i in range(K):
        if L[-1] != A[-i-1]:
            L.append(A[-i-1])
    
    L.pop(0)
    L_long = len(L)
    ans = [2,2]
    for i in range(L_long):
        s,t = ans[0],ans[1]
        ans[0] = -(-s//L[i])*L[i]
        ans[1] = (t//L[i] + 1)*L[i] - 1
        if ans[1] < ans[0]:
            print(-1)
            exit()
    
    print(ans[0],ans[1])
    
if __name__ == "__main__":
    main()
