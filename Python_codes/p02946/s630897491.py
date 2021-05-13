a = list(map(int,input().split()))
ans = ""
for i in range(a[1] - (a[0]-1),(a[0]-1)+a[1]+1):
    ans += str(i) + " "
print(ans)