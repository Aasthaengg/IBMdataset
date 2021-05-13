MOD = 10 ** 9 + 7
n = int(input())
s = input()

dic = {s[0]:1}
ans = 1
for i in range(1,n):
    if s[i] not in dic:
        ret = 1
        for v in dic.values():
            ret *= v + 1
            ret %= MOD
        ans += ret
        dic[s[i]] = 1
    else:
        ret = 1
        for k,v in dic.items():
            if k == s[i]:
                continue
            else:
                ret *= v + 1
                ret %= MOD
        ans += ret
        dic[s[i]] += 1
    ans %= MOD
print(ans)



