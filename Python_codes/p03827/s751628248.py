N = int(input())
S = input()

x = 0
max_num = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    if max_num < x:
        max_num = x
print(max_num)