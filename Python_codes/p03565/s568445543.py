#n,m = map(int,input().split())
#s,t = map(str,input().split())
#a = list(map(int,input().split()))
#m = list(map(str,input().split()))
#n = int(input())
#s = list(str(input()))
#s = str(input())
#t = str(input())

s_dash = list(str(input()))
t = list(str(input()))

lt = len(t)
ls = len(s_dash)
msg = "UNRESTORABLE"

#Tの方が長ければ不可能
if ls < lt:
    print(msg)
    exit()

#Sの候補を探す
candidate = []
for i in range(ls-lt+1):
    is_matched = True#TとS'の部分文字列が一致する可能性があるか
    tmp = s_dash.copy()

    for j in range(lt):
        if t[j] == s_dash[i+j] or s_dash[i+j] == '?':
            tmp[i+j] = t[j]
        else:
            is_matched = False
            break

    if is_matched == True:#一致する可能性があれば
        for j in range(ls):#残った'?'は'a'に置換
            if tmp[j] == '?':
                tmp[j] = 'a'
        
        cand = str("")
        for c in tmp:
            cand += c
        candidate.append(cand)

if len(candidate) == 0:
    print(msg)
else:
    candidate.sort()
    print(candidate[0])