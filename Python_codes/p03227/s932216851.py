import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(S):
    if len(S)==2:
        return S
    else:
        return S[::-1]
# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line = sys.stdin.readline().rstrip()
    return line

def main():
    n = readQuestion()
    answer = solve(n)
    print(answer)
    
if __name__ == '__main__':
    main()