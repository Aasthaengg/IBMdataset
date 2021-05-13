X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

eat = [p[i] for i in range(X)] + [q[i] for i in range(Y)]
eat.sort()
for i in range(len(r)):
    if eat[i] < r[i]:
        eat[i] = r[i]
    else:
        break

print(sum(eat))
