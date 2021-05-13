s = input()
ans = len(s)//2 - sum(c=='p' for c in s)
print(ans)
