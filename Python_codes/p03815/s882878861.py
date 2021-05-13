x = int(input())
ans = (x//11)*2 if x%11 == 0 else (x//11)*2 + 1 if x%11 <= 6 else (x//11)*2 + 2
print(ans)