import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def next_vary(S):
    if len(S) < 26:
        alpha = [0] * 26
        for s in S:
            alpha[ord(s) - 97] += 1
        add = None
        for i in range(26):
            if alpha[i] == 0:
                add = chr(i + 97)
                break
        S.append(add)
        return ''.join(S)
    
    else:
        before = set(S)
        flag = False
        for i in range(25,-1,-1):
            s = S[i]
            if s == 'z':
                before.discard('z')
                S.pop()
            else:
                asc = ord(s)
                for j in range(1,25):
                    if asc + j <= 122 and chr(asc + j) not in before:
                        S[i] = chr(asc + j)
                        flag = True
                        break
                if flag:
                    break
                before.discard(s)
                S.pop()
        return ''.join(S)

def main():
    S = input()
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        return
    
    ans = next_vary(list(S))
    print(ans)
if __name__ == '__main__':
    main()