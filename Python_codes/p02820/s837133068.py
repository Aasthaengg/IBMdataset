n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

kaburi = list(t)
for i in range(n-k):
    if kaburi[i] == kaburi[i+k]:
        kaburi[i+k] = 'x'
result = 0
for i in range(n):
    if kaburi[i] == 'r':
        result += p
    elif kaburi[i] == 's':
        result += r
    elif kaburi[i] == 'p':
        result += s
    else:
        pass


print(result)