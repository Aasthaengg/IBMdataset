S = input()
T = input()
ans = 'Yes' if S == T[:len(S)] else 'No'
print(ans)
