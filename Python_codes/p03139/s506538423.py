N, A, B = map(int, input().split())
 
ab = [A, B]
max_katu = min(ab)
 
if A+B >= N:
    min_katu = A+B-N
else:
    min_katu = 0
 
 
ans = [str(max_katu), str(min_katu)]
print(' '.join(ans))
