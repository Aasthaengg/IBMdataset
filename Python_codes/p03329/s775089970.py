n = int(input())


def saiki(tgt, i, count, ans):
    if i == 0 or tgt == 0:
        ans = min(tgt+count, ans)
        return ans

    num = tgt//temp[i]
    while num >= 0:
        nn = tgt - num*temp[i]
        ans = saiki(nn, i-1, count+num, ans)
        if ans < count+num:
            return ans
        num -= 1
    return ans


temp = [1]
a = 1
while n >= 6**a:
    temp.append(6**a)
    a += 1

b = 1
while n >= 9**b:
    temp.append(9**b)
    b += 1

temp.sort()
#print(temp)
print(saiki(n, len(temp)-1, 0, 10**9))
