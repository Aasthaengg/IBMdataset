n=int(input())

s=list(input())

ans = 0

for i in range(1000):
    i = str(i)
    keta = len(list(i))
    code = '0'*(3-keta)+i
    code = list(code)
    index = 0
    for j in s:
        if j == code[index]:
            index += 1
        if index == 3:
            break
    if index == 3:
        #print(code)
        ans += 1
print(ans)