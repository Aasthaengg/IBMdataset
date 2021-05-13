n = int(input())
li = list(map(int,input().split()))
ans = "Yes"
max_n = 0


for i in li:
    if i < max_n - 1:
        ans = "No"
        break
    max_n = max(i,max_n)
print(ans)