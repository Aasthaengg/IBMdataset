N = int(input())
s = [int(input()) for i in range(N)]

if all(i%10 == 0 for i in s):
    print(0)
    exit()

elif sum(s)%10 != 0:
    print(sum(s))
    exit()

test = []
s = sorted(s)
for i in s:
    test.append(i)

for i in range(N):
    test[i] = 0
    if sum(test)%10 != 0:
        print(sum(test))
        exit()
    else:
        test[i] = s[i]
