from collections import Counter
n, c, k = map(int, input().split())
time_people = Counter([int(input()) for _ in range(n)])
times = sorted(time_people.keys())
ans = 0
left = 0
right = 0
while time_people[times[-1]] > 0:
    space = c
    while times[left] + k >= times[right] and space > 0:
        new_passenger = min(c, time_people[times[right]])
        space -= new_passenger
        time_people[times[right]] -= new_passenger
        if right >= len(times):
            break
        if time_people[times[right]] == 0:
            right += 1
            if right == len(times):
                break
    ans += 1
    while left < len(times) and time_people[times[left]] <= 0:
        left += 1
print(ans)