Sp = input()
T = input()

if len(Sp) < len(T):
    print('UNRESTORABLE')
    exit(0)

candidates = []
for i in range(len(Sp) - len(T) + 1):
    x = Sp[i:i + len(T)]

    if all((x[idx] == '?' or x[idx] == T[idx] for idx in range(len(T)))):
        candidate = (Sp[:i] + T + Sp[i + len(T):]).replace('?', 'a')
        candidates.append(candidate)

if candidates:
    candidates.sort()
    print(candidates[0])
else:
    print('UNRESTORABLE')
