N = int(input())
S,T = input().split()

txt = ""

for i in range(N):
    txt += S[i]
    txt += T[i]

print(txt)