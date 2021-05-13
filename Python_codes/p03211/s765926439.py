S = input()

l = []
for i in range(3,len(S)+3):
    l.append(S[i-3:i])

ans = 100000000000
for i in l:
    if abs(int(i) - 753) < ans:
        ans = abs(int(i) - 753)

print(ans)