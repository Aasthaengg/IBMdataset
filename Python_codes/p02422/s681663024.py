"""
print a b: strの a 文字目から b 文字目までを出力する。
reverse a b: strの a 文字目から b 文字目までを逆順にする。
replace a b p: st の a 文字目から b 文字目までを p に置き換える
"""
s = str(input())
n_order = int(input())
# print(s)

for _ in range(n_order):
    list_order = [i for i in input().split(" ")]
    order = list_order[0]
    a = int(list_order[1])
    b = int(list_order[2])

    if order == 'print':
        s_a2b = s[a : b + 1]
        print(s_a2b)
    elif order == 'reverse':
        s_a2b = s[a : b + 1]
        s_a2b_rev = s_a2b[::-1]
        s = s[:a] + s_a2b_rev + s[b + 1:]
        # print("->",s)
    elif order == 'replace':
        p = str(list_order[3])
        s = s[:a] + p + s[b + 1:]
        # print("->", s)
    else:
        print("error")
        
    

