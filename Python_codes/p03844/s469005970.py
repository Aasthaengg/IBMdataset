li = input().split()
if li[1] == '+':
    ans = int(li[0]) + int(li[2])
else:
    ans = int(li[0]) - int(li[2])
print(str(ans))