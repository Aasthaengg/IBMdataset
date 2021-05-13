n = list(input())
k = int(input())
for i in range(min(len(n),k)):
    if n[i] != '1':
        print(n[i])
        exit()
print(1)