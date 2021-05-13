N, X = map(int, input().split())
l = list(map(int, input().split()))
l.insert(0, 0)
val, count = 0, 0
for i in l:
    val += i
    if val <= X:
        count += 1
    else:
        break
print(count)
