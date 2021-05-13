n = int(input())

ans=set()
for i in range(1,3 * int(n ** 0.5)):
    n -= i
    ans.add(i)
    if n < i + 1:
        ans.add(i + 1)
        no = i + 1 - n
        break

for i in ans:
    if i == no:
        continue
    print(i)