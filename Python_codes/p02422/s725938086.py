def _print(c):
    a,b = map(int,c)
    print(s[a:b+1])
def _reverse(c):
    global s
    a,b = map(int,c)
    r = s[b-len(s):a-len(s)-1:-1]
    s = s[0:a] + r + s[b+1:]
def _replace(c):
    global s
    a,b,p = c
    a = int(a)
    b = int(b)
    s = s[0:a] + p + s[b+1:]
s = input()
n = int(input())
command = {"print":_print,"reverse":_reverse,"replace":_replace}
for i in range(n):
        c = input().split()
        command[c[0]](c[1:])