N, A, B, C = map(int, input().split())
ABC = [A, B, C]
l = []
for _ in range(N):
    l.append(int(input()))

m = 10 ** 6
for choice in range(1, 4 ** (N + 1)):
    bucket = [[] for _ in range(4)]
    #print(choice)
    for j in range(N):
        temp = (choice // 4 ** j) % 4
        bucket[temp].append(l[j])
        #print(temp)
    #print(bucket)
    if bucket[0] and bucket[1] and bucket[2]:
        pass
    else:
        continue
    cost = 0
    for i in range(4):
        if i <= 2 and bucket[i]:
            if len(bucket[i]) >= 2:
                total = sum(bucket[i])
                cost += 10 * (len(bucket[i]) - 1)
            else:
                total = bucket[i][0]
            cost += abs(total - ABC[i])
    m = min(m, cost)
print(m)


