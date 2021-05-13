A,B=map(int,input().split())

n = 0
for i in range(A,B+1):
    s = str(i)
    recursive = True
    for j in range(len(s)//2):
        if s[j] != s[len(s)-1-j]:
            recursive = False
            break
    if recursive:
        n += 1

print(n)