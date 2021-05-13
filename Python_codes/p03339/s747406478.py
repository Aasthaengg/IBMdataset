import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N = int(readline())
    S = readline().rstrip().decode()
    #csw[i]:='W'のi番目までの登場回数
    #cse[i]:='E'のi番目までの登場回数
    csw = [0]
    cse = [0]
    for i in range(N):
        if S[i] == 'W':
            csw.append(csw[i]+1)
            cse.append(cse[i])
        else:
            csw.append(csw[i])
            cse.append(cse[i]+1)
    ans = int(1e6)
    for i in range(N):
        #Sのi番目の文字を見たときSの区間[0,i）にある'W'の数と区間(i, N)にある'E'の数の合計が「向く方向を変える人数」である
        #i番目はリーダーなので数えないことに注意
        ans = min(cse[N]-cse[i+1] + csw[i] - csw[0], ans)
    print(ans)
if __name__ == '__main__':
    main()
