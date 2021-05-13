import sys
input = sys.stdin.readline

s=input()
A = int(s[0])
B = int(s[1])
C = int(s[2])
D = int(s[3])

ans = ''
for i in range(2):
    if ans != '':
        break
    for j in range(2):
        if ans != '':
            break
        for k in range(2):
            t = A + (2*i-1)*B + (2*j-1)*C + (2*k-1)*D
            if t == 7:
                op1 = '-' if i == 0 else '+'
                op2 = '-' if j == 0 else '+'
                op3 = '-' if k == 0 else '+'
                ans = "{}{}{}{}{}{}{}=7".format(A,op1,B,op2,C,op3,D)
                break

print(ans)