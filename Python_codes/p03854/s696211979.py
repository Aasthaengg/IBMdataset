S=input()
S=S[::-1]

pointer=0
while 1:
  if pointer == len(S):
    print('YES')
    exit()
  if pointer >= len(S)-4:
    print('NO')
    exit()
  if S[pointer:pointer+5] in {'dream'[::-1],'erase'[::-1]}:
    pointer += 5
    continue
  elif S[pointer:pointer+6] == 'eraser'[::-1]:
    pointer += 6
    continue
  elif S[pointer:pointer+7] == 'dreamer'[::-1]:
    pointer += 7
    continue
  else:
    print('NO')
    exit()