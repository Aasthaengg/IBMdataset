ans = 0
n = int(input())
s = input()

for x in range(10):
    if s.find(str(x)) > -1:
        tmp = s[s.find(str(x)) + 1:]
        for y in range(10):
            if tmp.find(str(y)) > -1:
                tmp2 = tmp[tmp.find(str(y)) + 1:]
                for z in range(10):
                    if tmp2.find(str(z)) > -1:
                        ans += 1

print(ans)
