import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
# while 1:
if len(S)==26:
    end = S[-1]
    lis = [end]
    for i in range(24, -1, -1):
        if ord(S[i])<ord(end):
            for s in lis:
                if ord(S[i])<ord(s):
                    S[i] = s
                    break
            S = S[:i+1]
            print(''.join(S))
            break
        else:
            lis.append(S[i])
            end = S[i]
    else:
        if S[0]=='z':
            print(-1)
        else:
            S = [chr(ord(S[0])+1)]
            print(S[0])
else:
    check = [0]*26
    for s in S:
        check[ord(s)-97] = 1
    for i in range(26):
        if not check[i]:
            S.append(chr(i+97))
            break
    print(''.join(S))

