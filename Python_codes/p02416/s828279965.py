x = str(input())
while x != "0":
    ans = 0
    for i in list(x):
        ans += int(i)
    print(ans)
    x = str(input())