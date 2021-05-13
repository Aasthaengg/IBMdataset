def solver(s, k):
    res = 0
    cnt = [1]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt[-1] += 1
        else:
            cnt.append(1)
    for x in cnt:
        res += (x // 2) * k

    if len(cnt) == 1: #全部同じ場合はここでおわり
        return (len(s) * k) // 2

    if s[0] == s[-1]:
        res -= (cnt[0] // 2) * (k - 1) + (cnt[-1] // 2) * (k - 1)
        res += ((cnt[0] + cnt[-1]) // 2) * (k - 1)
    return res

def solver2(s, k):
    t = []
    for _ in range(k):
        t += s
    res = 0
    cnt = 1
    for i in range(1, len(t)):
        if t[i] == t[i - 1]:
            cnt += 1
        else:
            res += cnt // 2
            cnt = 1
    res += cnt // 2
    return res

s = input()
k = int(input())

#ss = s
#kk = k
print(solver(s, k))
#print(solver2(ss, kk))

#　ランダムな英小文字列の生成
import random
import string

# n := 文字列の長さ
def randomCharacter(n):
   alphabet_m = string.ascii_lowercase
   return ''.join([random.choice(alphabet_m) for _ in range(n)])


#for i in range(40):
#    if i == 0:
#        st = 'aaaaaaaaa'
#    elif i == 1:
#        st = 'a'
#    else:
#        l = random.randrange(1, 10)
#        st = randomCharacter(l)
#    sstt = st
#    cnt = 4
#    cnst_st = st[:]
#    res1 = solver(st, cnt)
#    res2 = solver2(sstt, cnt)
#    if res1 == res2:        
#        print("OK!")
#    else:
#        print(''.join(cnst_st), res1, res2)
        
