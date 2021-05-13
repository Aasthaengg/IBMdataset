S = input()[::-1]

dreams = ['dream', 'dreamer', 'erase', 'eraser']
dreams = [dream[::-1] for dream in dreams]

i = 0
while i < len(S):
    flag = False
    for j in dreams:
        if S[i:i+len(j)] == j:
            i = i + len(j)
            flag = True
    if not flag:
        break

print("YES" if flag else "NO")
