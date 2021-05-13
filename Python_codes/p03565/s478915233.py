def main():
    s = input()
    t = input()
    # ansはtを含む
    # tをいれられる場所を探す
    ans = []
    for i in range(len(s)-len(t)+1):
        tmp = s[:i]
        flag = False
        for j in range(i,i+len(t)):
            if s[j]==t[j-i]:
                tmp += t[j-i]
                pass
            elif s[j]=='?':
                tmp += t[j-i]
                pass
            else:
                flag = True
                break
        if not flag:
            tmp += s[i+len(t):]
            tmp = tmp.replace('?','a')
            ans.append(tmp)
    if ans:
        ans.sort()
        print(ans[0])
    else:
        print('UNRESTORABLE')

main()
