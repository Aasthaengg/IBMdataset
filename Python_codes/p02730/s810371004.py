s = input()
N = len(s)

s_first = s[:(N-1)//2]
s_second = s[(N+1)//2:]

if(s == s[::-1] and s_first == s_first[::-1] and s_second == s_second[::-1]):
    print("Yes")
else:
    print("No")
