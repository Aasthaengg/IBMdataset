import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')
kijun = ord("a")
if len(s) == 26:
    if s == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        exit()
    else:
        for i in range(26):
            res = s[i:]
            flag = True
            for j in range(len(res)-1):
                if ord(res[j]) < ord(res[j+1]):
                    flag = False
                    break
            if flag:
                ans = s[:i-1]
                res2 = []
                for j in res:
                    res2.append(ord(j))
                res2.sort()
                for j in res2:
                    if ord(s[i-1]) < j:
                        print(ans + chr(j))
                        exit()




for i in range(kijun,kijun+26):
    if chr(i) not in s:
        print(s+chr(i))
        exit()