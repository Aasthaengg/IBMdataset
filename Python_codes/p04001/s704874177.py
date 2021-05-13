S = input()

def rec(n, s):
    if n == 1:
        ans = 0
        for i in s.split("+"):
            ans += int(i)
        return ans
    
    # 文字列の後ろからn番目に"+"を入れるか否か
    return rec(n-1, s) + rec(n-1, s[:-n+1]+"+"+s[-n+1:])

print(rec(len(S), S))