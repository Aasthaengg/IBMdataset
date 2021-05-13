S = input()
prev = None
for s in S:
    if s == prev:
        print('Bad')
        break
    prev = s
else:
    print('Good')