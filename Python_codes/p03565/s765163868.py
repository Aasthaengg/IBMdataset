import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = readline().decode().rstrip()
t = list(readline().decode().rstrip())

L = []
for i in range(len(s)-len(t)+1):
    s1 = list(s)[:i:]
    s2 = list(s)[i::]
    is_ok = True

    for j in range(len(t)):
        if s2[j] == '?' or s2[j] == t[j]:
            s2[j] = t[j]
        else:
            is_ok = False
            break
    if is_ok:
        a = "".join(s1) + "".join(s2)
        a = a.replace('?', 'a')
        L.append(a)
L.sort()

print('UNRESTORABLE' if len(L) == 0 else L[0])