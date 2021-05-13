k, x = map(int, input().split())
ans = []
[ans.append(i) for i in range(x-k+1, x+k)]
s_ans = map(str, ans)
print(' '.join(s_ans))