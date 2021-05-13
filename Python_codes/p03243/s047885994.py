n = int(input())
div, mod = divmod(n, 111)
ans = div * 111 if mod == 0 else (div + 1) * 111
print(ans)
