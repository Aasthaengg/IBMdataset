N = int(input())
s = input()

S = sorted(s)
idx = N//2-1 if N%2==0 else N//2
ans = 'Yes' if S[idx] == 'R' else 'No'
print(ans)