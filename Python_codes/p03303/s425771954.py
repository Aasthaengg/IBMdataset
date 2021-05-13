S = input()
w = int(input())
a = len(S)//w
b = 1 if len(S) % w else 0
ans = ''
for i in range(a+b):
    ans += S[i*w]
print(ans)