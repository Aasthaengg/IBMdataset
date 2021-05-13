k = int(input())
s = input()

if len(s) <= k:
    print(s)
elif len(s) > k:
    s_k = s[0:k]
    print(s_k + "...")