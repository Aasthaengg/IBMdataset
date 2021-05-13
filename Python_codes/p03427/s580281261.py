n = list(input())
n = [int(i) for i in n]
digit = len(n)


if n[1:] == [9]*(digit-1):
    ans = sum(n)
else:
    ans = (n[0]-1)+9*(digit-1)
print(ans)