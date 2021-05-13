N = input()
a = int(N[-1])
if a == 3:
    ans = "bon"
elif a == 0 or a == 1 or a == 6 or a == 8:
    ans = "pon"
else:
    ans = "hon"

print(ans)