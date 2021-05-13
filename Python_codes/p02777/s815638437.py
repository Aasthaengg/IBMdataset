s = input().split()
t = list(map(int,input().split()))
d = {s[0]:t[0],s[1]:t[1]}
d[input()]-=1
print(d[s[0]], d[s[1]])