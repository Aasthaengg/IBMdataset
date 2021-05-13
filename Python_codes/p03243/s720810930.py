n = int(input())

a = 0
for i in range(1, 10):
    ans = [str(i)]*3
    ans_ = "".join(ans)
    if int(ans_) >= n:
        a = ans_
        if a != 0:
            break

print(int(a))