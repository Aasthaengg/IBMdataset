S = input()
rS = reversed(S)

print(sum([s != rs for s, rs in zip(S, rS)]) // 2)
