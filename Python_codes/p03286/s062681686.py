n = int(input())
i = 0
ans = []
if n == 0:
    print(0)
    quit()
while n:
    i += 1
    if n%(2**i):
        n -= (-2)**(i-1)
        ans.append("1")
    else:
        ans.append("0")
print("".join(ans[::-1]))
