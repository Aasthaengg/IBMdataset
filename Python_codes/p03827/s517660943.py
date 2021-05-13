n = int(input())
s = input()
x = 0
arr = [0]
d = {'I': 1, 'D': -1}
for i in range(n):
  x += d[s[i]]
  arr.append(x)
print(max(arr))