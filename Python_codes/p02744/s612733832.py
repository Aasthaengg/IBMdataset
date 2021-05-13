def dfs(s, mx):#sに対して、sと同じかsの一つ辞書順で後の文字列を追加する関数
    if len(s) == n:
        print(s)
        return
    for c in range(ord("a"), mx + 1):#
        dfs(s + chr(c), mx + 1 if c == mx else mx)#再帰的に一つ追加する

n = int(input())
dfs("", ord("a"))