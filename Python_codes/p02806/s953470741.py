n = int(input())
s, t  = [], []
for i in range(n):
    ST = list(map(str, input().split()))
    s.append(ST[0])
    t.append(int(ST[1]))

x = input()
idx = s.index(x)
print(sum(t[idx+1:]))