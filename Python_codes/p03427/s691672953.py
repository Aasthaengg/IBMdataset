n = str(int(input().rstrip())+1)
ans = (len(n)-1)*9
ans += (int(n[0])-1)
print(ans)