N,A,B = map(int,input().split())

max_ans = min(A,B)
if N-A-B>0:
    min_ans = 0
else:
    min_ans = abs(N-A-B)
print(max_ans, min_ans)