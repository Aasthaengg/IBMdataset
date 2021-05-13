N = int(input())
s = input()
t = input()
for i in range(0,N+1):
    ss = s[:i]+t
    if ss[:N] == s and ss[len(ss)-N:] == t:
        print(len(ss))
        exit()
