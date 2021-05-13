n = int(input())
sm = 0
b_first = 0
a_end = 0
b_a = 0

for i in range(n):
    s = input()
    for j in range(len(s)-1):
        if s[j]=="A" and s[j+1]=="B":
            sm += 1
    if s[0]=="B" and s[-1]=="A": b_a += 1    
    elif s[0]=="B": b_first += 1
    elif s[-1]=="A": a_end += 1

ans = sm

if b_a == 0:
    ans += min(b_first,a_end)
elif b_first+a_end==0:
    ans += b_a-1
else:
    ans += b_a + min(b_first, a_end)

print(ans)