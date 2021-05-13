N = int(input())

s = [None] * N
l, c, r = 0, N//2, N-1

while True:
    for i in (l, c, r):
        if s[i] == None:
            print(i, flush=True)
            s[i] = input()
            if s[i] == 'Vacant':
                exit()
    if ((c-l)%2==0 and s[l]!=s[c]) or ((c-l)%2 and s[l]==s[c]):
        r = c
        c = (l + r) // 2
    else:
        l = c
        c = (l + r) // 2
