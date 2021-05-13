cnt,ans = 0,0
for i in list(input()):
    if i in 'ACGT':
        cnt += 1
    else:
        cnt = 0
    ans = max(cnt,ans)
print(ans) 