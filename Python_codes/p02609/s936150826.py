def popcnt_int(n): # n:int
    return bin(n).count('1')

def popcnt_bin(s): # s:str
    return s.count('1')

def poptimes(n, cnt=1): #:int, popcntのcounter
    if n==0:
        return cnt
    else:
        n %= popcnt_int(n)
        cnt += 1
        return poptimes(n, cnt)

n = int(input())
s = input() #これが直接処理し難い大きさ → 一回目の処理に要工夫。
# 要:いずれかを反転させた場合のbitの数は'反転前のbit数±1'の2通り！

s_int = int(s,2) # 2進数で読み込む
pc = popcnt_bin(s)
pc_plus = s_int % (pc+1) # 予めs_intのmod(pc+1)を取得
if  pc != 1: # mod(pc-1)も同様だが, bitが1個だけの場合に反転すると全て'0'になるためこの場合だけ例外扱い。
    pc_minus = s_int % (pc-1)
#print(n,s,s_int,pc,pc_plus,pc_minus)

# 以下で反転した差分を処理(一回目の処理完了) → 二回目以降は処理対象の値が大きくないためそのまま処理(poptimes関数)すればOK
for i in range(n):
    if s[i] == '1': # 1から0へと減じた差分を処理 
        if pc != 1: # 例外を考慮
            tmp = pc_minus - pow(2, n-i-1, pc-1) # ここで差し引くが, 差分をmod(pc-1)で処理
            print(poptimes(tmp % (pc-1))) # poptimesへパスする前にもmod(pc-1)
        else: # 例外処理: pc=1(反転して全部'0')の場合
            print(0)
            continue
    
    else: # 0から1への差分を処理, 必ず一つはbitが立つので例外は考慮不要
        tmp = pc_plus + pow(2, n-i-1, pc+1)
        print(poptimes(tmp % (pc+1)))
