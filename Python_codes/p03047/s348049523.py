N,K = map(int,input().split())


s = []
for i in range(1,N + 1):
    s.append(str(i))

tmp = [''.join(s[i:i+K]) for i in range(len(s)-K+1)]


print(len(tmp))
