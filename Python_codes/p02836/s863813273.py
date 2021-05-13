s = list(input())

s1 = s[:len(s)//2]
s2 = s[-(-len(s)//2):][::-1]

cnt = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        s1[i] = s2[i]
        cnt += 1

print(cnt)