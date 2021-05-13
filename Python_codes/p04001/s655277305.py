S = input() #l桁の数字を文字列型で入力
l = len(S) # 文字列の長さ
n = l - 1 # 文字列の間の数
ans = 0
for bit in range(1 << n): # 0から((1をnだけ右シフトした数)-1)までのfor文
    s = S[0]
    for i in range(n):
        if (bit & (1 << i)):
            s += '+'
        s += S[i+1]
    ans += sum(map(int, s.split('+')))
print(ans)