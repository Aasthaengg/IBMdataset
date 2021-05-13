S = input()
key = 'keyence'
index_num = -1
for i in range(len(key)):
    if S[i] != key[i]:
        index_num = i
        break
else:
    print('YES')
    exit()
string = S[:index_num] + S[-len(key)+index_num:]
print('YES' if string == key else 'NO')