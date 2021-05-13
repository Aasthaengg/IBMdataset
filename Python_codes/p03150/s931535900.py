S = input()
ans = "keyence"
for i in range(7):
    #print(S[:i],ans[:i],S[-7+i:],ans[-7+i:])
    if S[:i] == ans[:i] and S[-7+i:] == ans[-7+i:]:
        print('YES')
        exit()
print('NO')
