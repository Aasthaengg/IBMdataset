# CODE FESTIVAL 2016 予選 B: A – Signboard
expects = 'CODEFESTIVAL2016'
s = input()
print(sum([a != b for a, b in zip(expects, s)]))