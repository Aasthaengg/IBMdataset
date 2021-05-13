s=input()
q=int(input())
for _ in range(0,q):
    ops = input().split()
    if ops[0] == 'print':
        a,b=map(int,ops[1:3])
        print(s[a:b+1])
    if ops[0] == 'reverse':
        a,b=map(int,ops[1:3])
        s = s[0:a] + s[a:b+1][::-1] + s[b+1:]
    if ops[0] == 'replace':
        a,b=map(int,ops[1:3])
        s = s[0:a] + ops[3] + s[b+1:]