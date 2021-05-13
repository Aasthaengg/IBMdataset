# https://atcoder.jp/contests/arc061/tasks/arc061_a

s = input()
k = len(s)

# def dfs(i, f) :
#     """
#     argument i : どこから始めるか
#     f :　最初の数
#     returen : falese or ture(作れるならtrue)
#     """
#     if i == k-1:
#         return sum(list(map(int, f.split('+'))))

#     return dfs(i+1, f + s[ i +1 ]) + \
#            dfs(i+1, f + '+' +  s[ i +1 ]) 

# print(dfs(0, s[0]))

#bit木を書いていきます

ans = 0

for bit in range(1 << (k-1)):
    f = s[0]
    
    for i in range(k-1):
        # if bit & (1 << i)で、bitにiが含まれているか（フラグが立っているか）を判定してくれるらしい
        if bit & (1 << i):
            f += '+'
        f += s[i + 1]
    ans += sum(list(map(int, f.split('+'))))

print(ans)