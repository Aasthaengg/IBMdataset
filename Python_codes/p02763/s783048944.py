from collections import defaultdict
import bisect

n = int(input())
s = input()
S = []
cnt_ch = defaultdict(list)
for i in range(n):
    S.append(s[i])
    cnt_ch[s[i]].append(i)
    
    
    
    
q = int(input())
for i in range(q):
    qw = input()
    if qw[0] == "1":
        qw = qw[2:]
        i, ch = map(str, qw.split())
        if S[int(i) - 1] == ch:
            continue
        remove = bisect.bisect_left(cnt_ch[S[int(i) - 1]], int(i) - 1)
        del cnt_ch[S[int(i) - 1]][remove]
        S[int(i) - 1] = ch
        if not cnt_ch[ch]:
            cnt_ch[ch].append(int(i) - 1)
            continue
        bisect.insort_left(cnt_ch[ch], int(i) - 1)
        
        
    else:
        #print(cnt_ch)
        qw = qw[2:]
        l, r = map(int, qw.split())
        cnt = 0
        for i in range(ord("a"),ord("a") + 26):
            if not cnt_ch[chr(i)]:
                continue
            edge = bisect.bisect_left(cnt_ch[chr(i)], l - 1)
            #print(cnt_ch[chr(i)][edge - 1:])
            #if bisect.bisect_left(cnt_ch[chr(i)][edge:], i) < r:
            #print(cnt_ch[chr(i)])
            #print(l, r)
            #print(edge)
            if edge < len(cnt_ch[chr(i)]):
                if cnt_ch[chr(i)][edge] < r:
                    cnt += 1
            #print(cnt, "cnt", chr(i))
        print(cnt)
        
        
