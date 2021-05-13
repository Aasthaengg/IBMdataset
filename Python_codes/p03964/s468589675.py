N = int(input())

l = [0, 0]
for _ in range(N):
    t, a = map(int, input().split())
    if t >= l[0] and a >= l[1]:
        l = [t, a]
    else:
        temp = max((l[0] - 1) // t + 1, (l[1] - 1) // a + 1)
        l = [t * temp, a * temp]
    
print(sum(l))