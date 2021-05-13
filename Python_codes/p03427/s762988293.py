S = input()
N = []
for s in S:
  N.append(int(s))

N.reverse()

ans = 0
for i in range(len(N)):
    if i != len(N)-1:
        ans += 9
        if N[i] != 9:
            N[i+1] -= 1
    else:
        ans += N[i]

print(ans)