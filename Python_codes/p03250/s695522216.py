a, b, c = map(int, input().split())
ans = []
ans.append(10* a + b + c)
ans.append(10* a + c + b)
ans.append(10* b+ a + c)
ans.append(10* b + c + a)
ans.append(10* c + a + b)
ans.append(10* c + b + a)
print(max(ans))