from itertools import product


N = int(input())
all_testimonies = []
for i in range(N):
    A = int(input())
    testimony = [list(map(int, input().split())) for _ in range(A)]
    all_testimonies.append({'A': A, 'test': testimony})
    
    
# bit全探索
for bits in sorted(product(*[range(2) for _ in range(N)]), key=lambda x: sum(x), reverse=True):
    valid = True
    for i,testimony in enumerate(all_testimonies):
        person_is_honest = bool(bits[i])
        if person_is_honest:
            for j,y in testimony['test']:
                if bits[j-1] == y:
                    continue
                valid = False
    if valid:
        print(sum(bits))
        break