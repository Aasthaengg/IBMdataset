N = int(input())
S, T = input().split()

print(''.join(S[i] + T[i] for i in range(N)))

# 上のワンライナーを長ったらしく書くとこう
# ans = str()
# for i in range(n):
#     ans += s[i]
#     ans += t[i]

# print(ans)