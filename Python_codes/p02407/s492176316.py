input()
i = list(map(int, input().split()))
i.reverse()
for j in range(len(i)) :
    if j != 0 :
        print(' ', end = '')
    print(i[j], end = '')
print()