import numpy as np

def main():
    s = input().split("T")
    x, y = map(int, input().split())
    xs = []
    x -= len(s[0])
    for i in range(2, len(s), 2):
        tmp = len(s[i])
        if tmp != 0:
            xs.append(tmp)
    ys = []
    for i in range(1, len(s), 2):
        tmp = len(s[i])
        if tmp != 0:
            ys.append(tmp)
    
    sum_x = sum(xs)
    sum_y = sum(ys)
    x = abs(x)
    y = abs(y)
    if sum_x < x or sum_y < y:
        print("No")
    else:
        rest_x = sum_x - x
        rest_y = sum_y - y
        if rest_x&1 or rest_y&1:
            print("No")
        else:
            ok = True
            if rest_x > 0:
                dp = np.array([[False]*8001 for i in range(len(xs)+1)])
                dp[0][0] = True
                for i in range(1, len(xs)+1):
                    dp[i] = dp[i] | dp[i-1]
                    dp[i][xs[i-1]:] = dp[i-1][xs[i-1]:] | dp[i-1][:-xs[i-1]]
                    # dp[i][:-xs[i-1]] = dp[i-1][:-xs[i-1]] | dp[i-1][xs[i-1]:]
                if not dp[-1][rest_x//2]:
                    ok = False
            if rest_y > 0:
                dp = np.array([[False]*8001 for i in range(len(ys)+1)])
                dp[0][0] = True
                for i in range(1, len(ys)+1):
                    dp[i] = dp[i] | dp[i-1]
                    dp[i][ys[i-1]:] = dp[i-1][ys[i-1]:] | dp[i-1][:-ys[i-1]]
                    # dp[i][:-ys[i-1]] = dp[i-1][:-ys[i-1]] | dp[i-1][ys[i-1]:]
                if not dp[-1][rest_y//2]:
                    ok = False
            if ok:
                print("Yes")
            else:
                print("No")
                    

if __name__ == "__main__":
    main()