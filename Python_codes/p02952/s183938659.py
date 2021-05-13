N = input()
ans = 0
for i in range(1,int(N)+1):
    if len(str(i)) % 2 == 1:
        ans += 1
    else:
        pass
print(ans)
