s = input()
left, right = [0,], [0,]
a, b = 0, 0
for i in range(len(s)):
    a = a+1 if s[i] == '<' else 0
    left.append(a)
    b = b+1 if s[-1*(i+1)] == '>' else 0
    right.append(b)

right.reverse()
ans = sum(max(x, y) for x, y in zip(left, right))
print(ans)