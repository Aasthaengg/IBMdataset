n, t = map(int, input().split())
people = list(map(int, input().split()))
people.append(people[-1]+ t+1)
if n == 1:
    print(t)
else:
    time = 0
    for i in range(n+1):
        if i ==0:
            togire = False
            start = people[i]
            continue
        if people[i] - people[i-1] > t:
            togire = True
            time += people[i-1] - start + t
            start = people[i]
        else:
            togire = False
    print(time)