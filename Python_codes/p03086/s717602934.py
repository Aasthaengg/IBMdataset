S=input()
ans=0
length=0
for c in S:
    if (c == 'A' or c == 'G' or c == 'C' or c == 'T'):
        length += 1
        if length > ans:
            ans = length
    else:
        length = 0

print(ans)
