
A = input()

dic = {}
num = 0
ans = 0

for s in A:

    if s in dic:
        ans += num - dic[s]
        dic[s] += 1

    else:
        ans += num
        dic[s] = 1

    num += 1

print (ans+1)
