N, A, B = map(int,input().split())
max_ans = min(A,B)
tmp = A + B - N
min_ans = 0 if tmp<=0 else tmp
print(max_ans, min_ans)