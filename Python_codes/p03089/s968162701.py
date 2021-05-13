n = int(input())
b = [int(i) for i in input().split()]
ans = []

for i in range(n):
    for j in range(n-i)[::-1]:
        k = j+1
        if b[j] == k:
            del b[j]
            ans.append(k)
            break
    else:
        ans = [-1]
        break

for i in ans[::-1]: print(i)