

def submit():
    n, c = map(int, input().split())
    table_max = 10 ** 5
    table = [0 for _ in range(table_max + 1)]

    programs = []
    for _ in range(n):
        s, t, c = map(int, input().split())
        programs.append((s, t, c))
    programs.sort(key=lambda x: (x[2], x[0]))

    program_merge = [programs[0]]
    last = programs[0]
    for p in programs[1:]:
        if last[2] == p[2] and last[1] == p[0]:
            program_merge.pop()
            program_merge.append((last[0], p[1], p[2]))
        else:
            program_merge.append(p)
        last = program_merge[-1]
            

    for s, t, _ in program_merge:
        table[s - 1] += 1
        table[t] -= 1

    curr_max = 0
    for i in range(1, table_max + 1):
        table[i] += table[i - 1]
        if table[i] > curr_max:
            curr_max = table[i]

    print(curr_max)


submit()