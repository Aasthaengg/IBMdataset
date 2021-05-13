n = int(input())
s = input()
t = input()
# print(s + t)
st = s + t
same = 0
for i in range(n):
    ok = True
    for j in range(i+1):
        if s[n-i+j-1] != t[j]:
            ok = False
        # print(i, j, ok)
    if ok:
        same = i+1
# print(same)
print(2*n - same)