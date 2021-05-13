n = int(input())
s = input()
s_w = [0] * (n)
s_e = [0] * (n)
ans = [0] * (n)

t = 0
for i in range(n-1):
    if s[i] == "W":
        t += 1
    s_w[i+1] += t
t = 0
for i in range(1,n):
    #print(s[-i])
    if s[-i] == "E":
        t += 1
    s_e[i] += t
s_e.reverse()
#print(s_w,s_e)
for i in range(n):
    ans[i] += s_w[i] + s_e[i]

print(min(ans))
