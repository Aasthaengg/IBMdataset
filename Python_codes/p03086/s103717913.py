s = input()
count = 0
ans = 0
for i in s:
    if i in "ACGT":
        count += 1
        ans = max(ans,count)
    else:
        count = 0
print(ans)