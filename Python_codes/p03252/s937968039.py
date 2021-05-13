import sys

readline = sys.stdin.readline

def myindex(l, s):
    if s in l:
        return l.index(s)
    else:
        return len(l)

def main():
    S = list(readline()[:-1])
    T = list(readline()[:-1])
    tmpS = []; tmpT = []
    cntS = 0; cntT = 0
    flag = True
    for i in range(len(S)):
        cntS = myindex(tmpS, S[i])
        cntT = myindex(tmpT, T[i])
        tmpS.append(S[i])
        tmpT.append(T[i])
        if cntS != cntT:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
