# aを1番目の値、2~n-1番目の値、n番目の値と3つに分けて考えてリストに追加
n = int(input())
b = list(map(int, input().split()))

a = []

# aの1番目の値
a.append(b[0])

# aの2~n-1番目の値
b_len = len(b)
for i in range(b_len-1):
    ai = min(b[i], b[i+1])
    a.append(ai)

# aのn番目の値
a.append(b[-1])

print(sum(a))