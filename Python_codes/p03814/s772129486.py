s = input()

left = s.index('A')+1
right = len(s)-s[::-1].index('Z')

ans = right - left + 1
print(ans)
