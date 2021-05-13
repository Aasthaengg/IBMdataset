a, b, c = map(int, input().split())
A = a % 2
B = b % 2
C = c % 2
cnt = 0
s = [a,b,c]
flag = [0,0,0,0]
if A == B == C:
    t = [a,b,c]
    t.sort()
    cnt = cnt + (t[2]-t[1])//2 + (t[2]-t[0])//2
    flag[0] += 1
elif A == B:
    cnt = cnt + 1
    a = a + 1
    b = b + 1
    t = [a,b,c]
    t.sort()
    cnt = cnt + (t[2]-t[1])//2 + (t[2]-t[0])//2
    flag[1] += 1
elif B == C:
    cnt = cnt + 1
    b = b + 1
    c = c + 1
    t = [a,b,c]
    t.sort()
    cnt = cnt + (t[2]-t[1])//2 + (t[2]-t[0])//2
    flag[2] += 1
elif C == A:
    cnt = cnt + 1
    c = c + 1
    a = a + 1
    t = [a,b,c]
    t.sort()
    cnt = cnt + (t[2]-t[1])//2 + (t[2]-t[0])//2
    flag[3] += 1
print(cnt)
# print(t)
# print(flag)