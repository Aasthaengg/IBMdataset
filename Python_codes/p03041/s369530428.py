n,k = map(int, input().split())
s = input()
s_s = s[:k-1]
s_l = s[k-1].lower()
s_e = s[k:]
print(s_s+s_l+s_e)