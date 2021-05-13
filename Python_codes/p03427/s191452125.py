x = int(input())
x += 1

ans = 9 * (len(str(x))-1) + int(str(x)[0])-1
print(ans)
