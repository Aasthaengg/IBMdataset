import itertools

N, M = map(int, input().split())
target_switches = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))


answer_count = 0
for switches in itertools.product((0, 1), repeat=N):
    on_count = 0
    for j in range(M):
        count = 0
        for i in range(N):
            if (switches[i] == 1) and (i + 1 in target_switches[j][1:]):
                count += 1
                
        if count % 2 == p[j]:
            on_count += 1
    
    if on_count == M:
        answer_count += 1

print(answer_count)