n = int(input())
s = input()
ecounter = [0 for _ in range(n)]
wcounter = [0 for _ in range(n)]
ecounter[0] = int(s[0]=='E')
wcounter[n-1] = int(s[n-1]=='W')
ans = n
for i in range(n-1):
    ecounter[i+1] = ecounter[i] + (s[i+1]=='E')
    wcounter[n-2-i] = wcounter[n-1-i] + (s[n-2-i]=='W')
for j in range(n):
    cnt = n - (ecounter[j]+wcounter[j])
    ans = min(cnt,ans)
print(ans)