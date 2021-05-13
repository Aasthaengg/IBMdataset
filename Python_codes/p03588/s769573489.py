a = int(input())
l =[]
for i in range(a):
    s = input().split(" ")
    n = int(s[0]); m = int(s[1])
    l.append(m+n)
print(min(l))