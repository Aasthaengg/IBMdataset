s = input()
print('Good' if all(si != sj for si, sj in zip(s, s[1:])) else 'Bad')
