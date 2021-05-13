n = (int)(input())
s, t, = map(str, input().split())

ret = ""
for i in range(n):
    ret += s[i]
    ret += t[i]

print("{}".format(ret))