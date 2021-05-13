# CODE FESTIVAL 2016 予選 B: A – Signboard
expects = 'CODEFESTIVAL2016'
s = input()

count = 0

for a, b in zip(expects, s):
    if a != b:
        count += 1

print(count)