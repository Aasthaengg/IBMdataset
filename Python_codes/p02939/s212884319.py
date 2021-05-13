import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    S = input()
    N = len(S)
    preString = 'A'
    i = 0
    cnt = 0
    #Sを前から調べる
    while i < N: 
        #Sをは切り出す最後尾の位置を示すポインタ
        #文字列に差異が出るまでjをインクリメントしていく
        j = i + 1
        while j <= N:
            if preString == S[i:j]:
                #一致したらjを次の位置に変更する
                j += 1
            else:
                #一致しなかったところで切り出すのでカウントする
                cnt += 1
                preString = S[i:j]
                break
            #先頭のポインタをjにする
        i = j
    print(cnt)
if __name__ == '__main__':
    main()
