n = int(input())
d = sorted(list(int(input()) for _ in range(n)))[::-1]
ans = [d[0]]

for i in d[1:]:
    if ans[-1] > i:
        ans.append(i)
print(len(ans))