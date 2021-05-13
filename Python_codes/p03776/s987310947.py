# D - Maximum Average Sets

N, A, B = map(int, input().split())
v = sorted(list(map(int, input().split())), reverse = True)

factorial_memo = [1]
for i in range(1,N+1):
    factorial_memo.append(factorial_memo[-1] * i)

def comb(n, r):
    return factorial_memo[n]//(factorial_memo[n-r] * factorial_memo[r])

print(sum(v[:A]) / A)
for i in reversed(range(A, N)):
    if v[i] == v[0]:
        print(sum([comb(i+1, x) for x in range(A, B+1)]))
        break
else:
    print(comb(v.count(v[A]), v[:A].count(v[A])))