from collections import deque

h, w = map(int,input().split())
S = [input() for _ in range(h)]
s = deque([(0,0)])  # サーチstack. 初期条件を設定
e = [[-1] * w for _ in range(h)]  # 探索済みノード集（総数Nを入れる）
e[0][0] = 0

def main():
    while len(s) > 0:  # len(s) > 0 でループ
        t = s.popleft()
        if is_end(t):  # 終了条件を満たすなら脱出
            break
        for i in get_children(t):  # t の子ノードを列挙
            if is_legal(i):  # i が探索対象として適切なら(この判定はget_children内でも可)
                if e[i[0]][i[1]] != -1:  # iが探索済みなら次へ(この判定はget_children内でも可)
                    continue
                s.append(i)
                e[i[0]][i[1]] = e[t[0]][t[1]] + 1 # 探索済としつつ距離を入れる
    cnt = 0
    for x in S:
        cnt += x.count(".")
    end = e[h-1][w-1]
    #printing()
    if end == -1:
        print(-1)
    else:
        print((cnt-2)-(end-1))
    
def printing():
    for i in range(len(e)):
        for j in range(len(e[i])):
            if e[i][j] == -1:
                print(S[i][j], end="")
            else:
                print(e[i][j], end="")
        print("")
    
def is_end(t):
    return t[0] == h-1 and t[1] == w-1

def get_children(t):
    return ((t[0]-1,t[1]),(t[0]+1,t[1]),(t[0],t[1]-1),(t[0],t[1]+1))

def is_legal(i):
    return -1 < i[0] < h and -1 < i[1] < w and S[i[0]][i[1]] == "."

if __name__ == "__main__":
    main()