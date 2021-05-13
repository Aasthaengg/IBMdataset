import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N = int(readline())
    chars = readline().decode()

    cntW = [0]
    cntR = [0] 
    for i in range(N):
        cntW.append(cntW[i] + (1 if chars[i] == 'W' else 0))
        cntR.append(cntR[i] + (1 if chars[i] == 'R' else 0))

    ans = int(1e9)
    for i in range(N+1):
        leftW = cntW[i]
        rightR = cntR[N]-cntR[i] 

        if leftW <= rightR:
            tmp = leftW + (rightR - leftW)
        else:
            tmp = rightR + (leftW - rightR)
        ans = min(tmp, ans)
    print(ans)
if __name__ == '__main__':
    main()
