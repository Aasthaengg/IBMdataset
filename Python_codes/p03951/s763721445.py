n = int(input())
s = str(input())
t = str(input())

if s == t:
    print(n)
    exit()

for i in range(1, n):
    s_ = s[i:n]
    t_ = t[0:n-i]
    if s_ == t_:
        ans = s[:i]+t
        print(len(ans))
        exit()
else:
    print(2*n)
