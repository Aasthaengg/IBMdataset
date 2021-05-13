s = input()
list_s = list(s)
len_s = len(list_s)
check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(26):
    if check[i] not in list_s:
        print(s + check[i])
        exit()
for i in range(1, len_s + 1):
    memo = list_s.pop(len_s - i)
    for j in range(check.index(memo) + 1, 26):
        if check[j] not in list_s:
            print(s[:26 - i] + check[j])
            exit()
print(-1)
