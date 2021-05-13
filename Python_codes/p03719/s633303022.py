a,b,c = map(int, input().split())
ans = "Yes"
if a<=c and c<=b:
    print(ans)
else:
    ans = "No"
    print(ans)