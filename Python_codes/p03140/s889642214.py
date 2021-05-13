n = int(input())
s = [input() for _ in range(3)]

ans = 0
for v in zip(*s):
    len_ = len(set(v))
    ans += len_ - 1

    # if len_ == 3:
    #     ans += 2
    # elif len_ == 2:
    #     ans += 1
    # else:
    #     # len_ == 1
    #     ans += 0

print(ans)
