s = str(input())
n = int(input())

for i in range(n):
    x = list(map(str,input().split()))
    x[1],x[2] = (int(x[1]),int(x[2]))
    if x[0] == 'print':
        print(s[x[1]:(x[2]+1)])
    if x[0] == 'reverse':
        s = s[:x[1]] + s[x[1]:(x[2]+1)][::-1] + s[x[2]+1:]
    if x[0] == 'replace':
        s = s[:x[1]] + x[3] + s[x[2]+1:]
