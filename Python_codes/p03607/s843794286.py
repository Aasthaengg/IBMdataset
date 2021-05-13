#https://atcoder.jp/contests/abc073/tasks/abc073_c
N = int(input())
N_Dict = {}
for i in range(N):
    moji = str(input())
    if moji in N_Dict:
        N_Dict.pop(moji)
    else:
        N_Dict[moji] = 1
print(len(N_Dict))