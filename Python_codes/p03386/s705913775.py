A, B, K = map(int, input().split())
candidate1 = [i for i in range(A, A+K) if i <= B]
candidate2 = [i+1 for i in range(B-K, B) if i+1 >= A]

ans = list(sorted(list(set(candidate1+candidate2))))
ans = [str(ans[i]) for i in range(len(ans))]

print('\n'.join(ans))