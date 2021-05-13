List = [int(n) for n in input()]
ans = [List[0]] * 4
for i in range(8):
    for j in range(3):
        if i & (1<<j):
            ans[j+1]= -List[j+1]
        else:
            ans[j+1] = List[j+1]
    if sum(ans) == 7:
        break
ans = [str(ans[0])] + ['+' + str(x) if x>=0 else str(x) for x in ans[1:]]
print("".join(ans) + '=7')