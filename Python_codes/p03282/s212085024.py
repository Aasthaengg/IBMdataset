S = input()
K = int(input())

count = 0
xString = ''
for i in range(len(S)):
    if S[i] == '1':
        count += 1
    else:
        xString = S[i]
        break

if K <= count:
    print(1)
else:
    print(xString)