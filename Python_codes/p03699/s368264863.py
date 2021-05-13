
N = int(input())
s = []
for i in range(N):
    s.append(int(input()))

s = sorted(s)
total = sum(s)

if total%10!=0:
    out=total
    print(out)
else:
    scr=total
    for i in range(N):
        if s[i] %10!=0:
            print(sum(s)-s[i])
            break
        elif i==N-1:
            print(0)
            break